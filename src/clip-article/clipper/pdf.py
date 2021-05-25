# -*- coding: utf-8 -*-
"""PDF Reader and Writer Classes."""
import os

import PyPDF4

from PyPDF4.pdf import PdfFileReader
from PyPDF4.generic import ArrayObject
from PyPDF4.generic import DecodedStreamObject
from PyPDF4.generic import DictionaryObject
from PyPDF4.generic import NameObject
from PyPDF4.generic import createStringObject


class PdfFileWriter(PyPDF4.pdf.PdfFileWriter):
    """Include add multiple attachments method from head"""

    def attach_files(self, attachments, cut_paths=True):
        """
        Embed multiple files inside the PDF.
        Similar to addAttachment but receives a file path or a list of file paths.
        Allows attaching more than one file.
        :param files: Single file path (string) or multiple file paths (list of strings).
        :param cut_paths: Display file name only in PDF if True,
                        else display full parameter string or list entry.

        Modded:
        1. Change name of self._root_object to match current.
        2. Accept list of pathlib.objects instead of strings
        3. Only accepts [files] and not file
        """
        files_array = ArrayObject()

        for file in [x.as_posix() for x in attachments]:
            fname = file
            if cut_paths:
                fname = os.path.basename(fname)
            fdata = open(file, "rb").read()

            # The entry for the file
            file_entry = DecodedStreamObject()
            file_entry.setData(fdata)
            file_entry.update({NameObject("/Type"): NameObject("/EmbeddedFile")})

            # The Filespec entry
            efEntry = DictionaryObject()    # pylint: disable=invalid-name
            efEntry.update({NameObject("/F"): file_entry})

            filespec = DictionaryObject()
            filespec.update(
                {
                    NameObject("/Type"): NameObject("/Filespec"),
                    NameObject("/F"): createStringObject(fname),
                    NameObject("/EF"): efEntry,
                }
            )

            files_array.extend([createStringObject(fname), filespec])

        # The entry for the root
        embeddedFilesNamesDictionary = DictionaryObject() # pylint: disable=invalid-name
        embeddedFilesNamesDictionary.update({NameObject("/Names"): files_array})

        embeddedFilesDictionary = DictionaryObject() # pylint: disable=invalid-name
        embeddedFilesDictionary.update(
            {NameObject("/EmbeddedFiles"): embeddedFilesNamesDictionary}
        )

        # Update the root
        self._root_object.update({NameObject("/Names"): embeddedFilesDictionary})


def add_attachments(pdf_in, pdf_out, attachments):
    """Embedd atachments within PDF file.

    :param pdf_in: path to source pdf file
    :type pdf_in: Path()
    :param pdf_out: path to output pdf file
    :type pdf_out: Path()
    :param attachments: List of file attachment paths
    :type attachments: [Path()]
    :return: None
    """
    reader = PdfFileReader(pdf_in.as_posix())
    writer = PdfFileWriter()

    writer.appendPagesFromReader(reader)
    writer.attach_files(attachments)

    with pdf_out.open('wb') as fd_out:
        writer.write(fd_out)
