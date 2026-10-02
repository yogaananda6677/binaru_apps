#!/usr/bin/env python3
"""Complete the PKL journal while preserving the original DOCX formatting."""

from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import re
from tempfile import NamedTemporaryFile
from xml.etree import ElementTree as ET
from zipfile import ZIP_DEFLATED, ZipFile


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
CP_NS = "http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
DCTERMS_NS = "http://purl.org/dc/terms/"
W = f"{{{W_NS}}}"

NAMESPACES = {
    "wpc": "http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas",
    "mc": "http://schemas.openxmlformats.org/markup-compatibility/2006",
    "o": "urn:schemas-microsoft-com:office:office",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "m": "http://schemas.openxmlformats.org/officeDocument/2006/math",
    "v": "urn:schemas-microsoft-com:vml",
    "wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing",
    "w": W_NS,
    "wpg": "http://schemas.microsoft.com/office/word/2010/wordprocessingGroup",
    "wpi": "http://schemas.microsoft.com/office/word/2010/wordprocessingInk",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "wne": "http://schemas.microsoft.com/office/word/2006/wordml",
    "wps": "http://schemas.microsoft.com/office/word/2010/wordprocessingShape",
    "w10": "urn:schemas-microsoft-com:office:word",
    "wp14": "http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing",
    "w14": "http://schemas.microsoft.com/office/word/2010/wordml",
    "w15": "http://schemas.microsoft.com/office/word/2012/wordml",
    "w16cex": "http://schemas.microsoft.com/office/word/2018/wordml/cex",
    "w16cid": "http://schemas.microsoft.com/office/word/2016/wordml/cid",
    "w16": "http://schemas.microsoft.com/office/word/2018/wordml",
    "w16sdtdh": "http://schemas.microsoft.com/office/word/2020/wordml/sdtdatahash",
    "w16se": "http://schemas.microsoft.com/office/word/2015/wordml/symex",
}
for namespace_prefix, namespace_uri in NAMESPACES.items():
    ET.register_namespace(namespace_prefix, namespace_uri)

SOURCE = Path(
    "/home/yoga/Data/Laporan PKL/PELAKSANAAN PKL/"
    "Jurnal Kegiatan Praktik Kerja Lapangan 2026 - dilengkapi sampai 1 Agustus.docx"
)
OUTPUT = Path("Jurnal_Kegiatan_PKL_2026_Lengkap.docx")


NEW_ENTRIES = [
    (
        "29 Juli 2026",
        "Peninjauan alur sinkronisasi scan packing",
        "Meninjau alur antrean scan packing dari aplikasi mobile ke backend, memeriksa perubahan status paket, serta mencatat kondisi yang berpotensi menimbulkan perbedaan data antara penyimpanan lokal dan server.",
    ),
    (
        "3 Agustus 2026",
        "Evaluasi hasil pengujian regresi Jeejak",
        "Mengevaluasi catatan pengujian scan packing, dropping, retur, autentikasi, dan sinkronisasi bukti. Mengelompokkan temuan berdasarkan bagian mobile dan backend serta menyiapkan langkah verifikasi lanjutan.",
    ),
    (
        "5 Agustus 2026",
        "Pemeriksaan validasi data sinkronisasi",
        "Memeriksa validasi payload dan respons API pada proses sinkronisasi aktivitas. Menguji penanganan data kosong, status yang tidak sesuai, dan kegagalan jaringan agar aplikasi dapat menampilkan informasi yang jelas kepada pengguna.",
    ),
    (
        "6 Agustus 2026",
        "Pengujian ulang autentikasi mobile dan backend",
        "Menguji proses login, penggunaan token, masa berlaku sesi, dan akses endpoint yang memerlukan autentikasi. Memastikan request tanpa kredensial yang valid ditolak dan pengguna diarahkan kembali ke halaman login.",
    ),
    (
        "7 Agustus 2026",
        "Perapian penanganan kesalahan aplikasi",
        "Meninjau pesan kesalahan pada proses pemindaian dan sinkronisasi, lalu menyelaraskan penanganan kondisi gagal agar mudah dipahami. Melakukan pengujian pada skenario koneksi terputus dan respons server tidak berhasil.",
    ),
    (
        "8 Agustus 2026",
        "Verifikasi data bukti dropping dan retur",
        "Membandingkan data bukti dropping dan retur pada aplikasi mobile, API backend, dan web console. Memastikan berkas media, informasi provider, nomor resi, dan status aktivitas ditampilkan secara konsisten.",
    ),
    (
        "11 Agustus 2026",
        "Pengujian batas kuota dan paket pengguna",
        "Menguji pembatasan jumlah toko dan kuota impor resi pada beberapa kondisi paket. Memastikan validasi backend sesuai dengan informasi kuota pada antarmuka serta tidak mengganggu data yang sudah tersimpan.",
    ),
    (
        "12 Agustus 2026",
        "Peninjauan alur upgrade dan pembayaran",
        "Meninjau kembali alur upgrade paket melalui hosted checkout, termasuk penggunaan kupon, pembentukan payload, dan pembaruan status langganan. Mencatat hasil pengujian untuk skenario berhasil, dibatalkan, dan data opsional kosong.",
    ),
    (
        "13 Agustus 2026",
        "Pengujian role dan hak akses anggota tim",
        "Menguji undangan anggota tim dengan role admin dan operator, redirect setelah login, serta pembatasan menu berdasarkan hak akses. Memastikan pengguna hanya dapat menjalankan fungsi yang sesuai dengan perannya.",
    ),
    (
        "14 Agustus 2026",
        "Pemeriksaan konsistensi sesi aktivitas",
        "Memeriksa aturan satu sesi aktif untuk aktivitas packing, dropping, dan retur. Menguji pembuatan, pelanjutan, serta penyelesaian sesi untuk memastikan tidak muncul sesi ganda atau status yang tertinggal.",
    ),
    (
        "15 Agustus 2026",
        "Dokumentasi hasil pengujian backend dan mobile",
        "Merapikan catatan pengujian, langkah reproduksi masalah, hasil yang diharapkan, dan hasil aktual. Menyusun dokumentasi singkat agar temuan dapat ditindaklanjuti pada pengembangan backend maupun aplikasi mobile.",
    ),
    (
        "18 Agustus 2026",
        "Pengujian integrasi scan packing",
        "Menjalankan pengujian menyeluruh mulai dari pemindaian resi, validasi status, penyimpanan antrean, hingga sinkronisasi ke backend. Memastikan paket yang telah diproses tidak dapat dipindai ulang.",
    ),
    (
        "19 Agustus 2026",
        "Pengujian ketahanan sinkronisasi data",
        "Menguji proses sinkronisasi ketika koneksi tidak stabil dan request perlu dicoba kembali. Memastikan data lokal tetap tersimpan, tidak terkirim ganda, dan status terbaru dari backend digunakan setelah sinkronisasi berhasil.",
    ),
    (
        "20 Agustus 2026",
        "Evaluasi akhir dan rekap pekerjaan Jeejak",
        "Melakukan pengujian regresi akhir pada fitur utama web console, backend, dan mobile. Merekap perbaikan, hasil pengujian, serta pekerjaan yang masih perlu dipantau sebagai bahan laporan dan serah terima kegiatan PKL.",
    ),
]


def cell_text(cell):
    return "".join((node.text or "") for node in cell.findall(f".//{W}t")).strip()


def set_cell_text(cell, value):
    paragraphs = cell.findall(f"./{W}p")
    if not paragraphs:
        paragraphs = [ET.SubElement(cell, f"{W}p")]
    paragraph = paragraphs[0]
    runs = paragraph.findall(f"./{W}r")
    if not runs:
        runs = [ET.SubElement(paragraph, f"{W}r")]
    texts = runs[0].findall(f"./{W}t")
    if not texts:
        texts = [ET.SubElement(runs[0], f"{W}t")]
    texts[0].text = value
    for node in texts[1:]:
        node.text = ""
    for run in runs[1:]:
        for node in run.findall(f".//{W}t"):
            node.text = ""
    for extra in paragraphs[1:]:
        for node in extra.findall(f".//{W}t"):
            node.text = ""


def set_row(row, values):
    cells = row.findall(f"./{W}tc")
    if len(cells) != 3:
        raise ValueError(f"Expected three cells, found {len(cells)}")
    for cell, value in zip(cells, values):
        set_cell_text(cell, value)


def set_cell_lines(cell, lines):
    paragraphs = cell.findall(f"./{W}p")
    while len(paragraphs) < len(lines):
        paragraphs.append(ET.SubElement(cell, f"{W}p"))
    for paragraph, value in zip(paragraphs, lines):
        runs = paragraph.findall(f"./{W}r")
        if not runs:
            runs = [ET.SubElement(paragraph, f"{W}r")]
        texts = runs[0].findall(f"./{W}t")
        if not texts:
            texts = [ET.SubElement(runs[0], f"{W}t")]
        texts[0].text = value
        for run in runs:
            for text_node in run.findall(f"./{W}t"):
                if text_node is not texts[0]:
                    text_node.text = ""
    for paragraph in paragraphs[len(lines):]:
        for text_node in paragraph.findall(f".//{W}t"):
            text_node.text = ""


def set_signature(signature_table):
    cells = signature_table.findall(f"./{W}tr/{W}tc")
    if len(cells) < 3:
        raise ValueError("Unexpected signature table structure")
    set_cell_lines(
        cells[0],
        [
            "Menyetujui,",
            "Pembimbing PKL",
            "",
            "",
            "Fadelis Sukya, S.Kom., M.Cs.",
            "NIDN. 0730038201",
        ],
    )
    set_cell_lines(
        cells[2],
        [
            "Kediri, 04 September 2026",
            "Pembimbing Lapangan",
            "",
            "",
            "Samsul Hadi, S.Kom., M.I.M.",
            "NIK. 1108081401",
        ],
    )


def page_break_paragraph():
    paragraph = ET.Element(f"{W}p")
    run = ET.SubElement(paragraph, f"{W}r")
    br = ET.SubElement(run, f"{W}br")
    br.set(f"{W}type", "page")
    return paragraph


def main():
    with ZipFile(SOURCE) as source_zip:
        document = ET.fromstring(source_zip.read("word/document.xml"))
        body = document.find(f"{W}body")
        tables = body.findall(f"./{W}tbl")
        activity_tables = [table for table in tables if len(table.findall(f"./{W}tr")) > 1]
        signature_tables = [table for table in tables if len(table.findall(f"./{W}tr")) == 1]

        # Complete and chronologically reorder the fourth page (29 July was missing).
        existing_rows = activity_tables[-1].findall(f"./{W}tr")
        prior_entries = []
        for row in existing_rows[2:5]:
            cells = row.findall(f"./{W}tc")
            prior_entries.append(tuple(cell_text(cell) for cell in cells))
        page_four_entries = [NEW_ENTRIES[0], *prior_entries, *NEW_ENTRIES[1:4]]
        for row, entry in zip(existing_rows[2:9], page_four_entries):
            set_row(row, entry)

        # Every page gets the verified names and signing date from the attendance form.
        for table in signature_tables:
            set_signature(table)

        # Add two more pages, retaining the exact table and approval-block styling.
        template_activity = activity_tables[-1]
        template_signature = signature_tables[-1]
        remaining = NEW_ENTRIES[4:]
        sections = [remaining[:7], remaining[7:]]
        sect_pr = body.find(f"./{W}sectPr")
        insert_at = list(body).index(sect_pr)

        for entries in sections:
            activity = deepcopy(template_activity)
            rows = activity.findall(f"./{W}tr")
            for row in rows[2:]:
                set_row(row, ("", "", ""))
            for row, entry in zip(rows[2:], entries):
                set_row(row, entry)
            signature = deepcopy(template_signature)
            set_signature(signature)

            for node in (page_break_paragraph(), activity, ET.Element(f"{W}p"), signature):
                body.insert(insert_at, node)
                insert_at += 1

        document_xml = ET.tostring(document, encoding="utf-8", xml_declaration=True)
        # ElementTree drops namespace declarations referenced only by mc:Ignorable.
        # Reinsert them so Word/OnlyOffice does not repair away the document tables.
        xml_text = document_xml.decode("utf-8")
        root_end = xml_text.index(">", xml_text.index("<w:document"))
        root_tag = xml_text[xml_text.index("<w:document"):root_end]
        missing = [
            f' xmlns:{prefix}="{uri}"'
            for prefix, uri in NAMESPACES.items()
            if not re.search(rf"\bxmlns:{re.escape(prefix)}=", root_tag)
        ]
        if missing:
            xml_text = xml_text[:root_end] + "".join(missing) + xml_text[root_end:]
        document_xml = xml_text.encode("utf-8")

        with NamedTemporaryFile(delete=False, suffix=".docx", dir=OUTPUT.parent) as temp:
            temp_path = Path(temp.name)
        with ZipFile(temp_path, "w", ZIP_DEFLATED) as output_zip:
            for item in source_zip.infolist():
                data = source_zip.read(item.filename)
                if item.filename == "word/document.xml":
                    data = document_xml
                elif item.filename == "docProps/core.xml":
                    core = ET.fromstring(data)
                    modified = core.find(f"{{{DCTERMS_NS}}}modified")
                    if modified is not None:
                        modified.text = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                    data = ET.tostring(core, encoding="utf-8", xml_declaration=True)
                output_zip.writestr(item, data)
        temp_path.replace(OUTPUT)

    print(OUTPUT.resolve())


if __name__ == "__main__":
    main()
