// pdf 한번에 보여주기

import React, { useState } from 'react';
import { Document, Page, pdfjs } from 'react-pdf';
import ReactPaginate from 'react-paginate'
import 'react-pdf/dist/Page/AnnotationLayer.css';
import 'react-pdf/dist/Page/TextLayer.css';


//pdfjs.GlobalWorkerOptions.workerSrc = `//unpkg.com/pdfjs-dist@${pdfjs.version}/build/pdf.worker.min.mjs`;
pdfjs.GlobalWorkerOptions.workerSrc = "/pdf.worker.mjs";

export function PdfPagination(fileInfo) {
  const [numPages, setNumPages] = useState(null);
  const [pageNumber, setPageNumber] = useState(fileInfo.fileInfo[1]);
  const pageCount = Math.ceil(numPages)

  function onDocumentLoadSuccess({ numPages }) {
    setNumPages(numPages);
    setPageNumber(fileInfo.fileInfo[1]);
    console.log("hello document!")
  }

  const handlePageClick = (event) => {
    const selectedPage = event.selected + 1;
    //console.log(
    //  `User requested page number ${event.selected}`
    //);
    setPageNumber(selectedPage);
  };
  //console.log(fileInfo.fileInfo)
  console.log(fileInfo.fileInfo[0])
  console.log(fileInfo.fileInfo[1])

  return (
    <>
      <div>
        <ReactPaginate
          breakLabel="..."
          previousLabel="<"
          nextLabel=">"
          onPageChange={handlePageClick}
          pageCount={pageCount}
          containerClassName="pagination"
          activeClassName="active"
          initialPage={fileInfo.fileInfo[1]-1}
          loading="<p>파일을 불러오는 중입니다...</p>"
          />
        <p className="pagination-current-page">
          Page {pageNumber || (numPages ? 1 : '--')} of {numPages || '--'}
        </p>
      </div>
      <Document
        key={fileInfo.fileInfo[0]}
        file={fileInfo.fileInfo[0]}
        onLoadSuccess={onDocumentLoadSuccess}
      >
        <Page pageNumber={pageNumber} width="800" />
      </Document>
    </>
  );
}

