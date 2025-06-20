// pdf 정해진 페이지 보여주기
import React, { useState } from 'react';
import { Document, Page, pdfjs } from 'react-pdf';
//import ReactPaginate from 'react-paginate'
import 'react-pdf/dist/Page/AnnotationLayer.css';
import 'react-pdf/dist/Page/TextLayer.css';

//pdfjs.GlobalWorkerOptions.workerSrc = `//unpkg.com/pdfjs-dist@${pdfjs.version}/build/pdf.worker.min.mjs`;
pdfjs.GlobalWorkerOptions.workerSrc = "/pdf.worker.mjs";

export function PdfView(fileInfo) {
  const [numPages, setNumPages] = useState(null);
  const [pageNumber, setPageNumber] = useState(fileInfo.fileInfo[1]);
  //const pageCount = Math.ceil(numPages)

  function onDocumentLoadSuccess({ numPages }) {
    setNumPages(numPages);
    setPageNumber(fileInfo.fileInfo[1]);
    console.log("hello document!")
  }

  // const handlePageClick = (event) => {
  //   const selectedPage = event.selected + 1;
  //   //console.log(
  //   //  `User requested page number ${event.selected}`
  //   //);
  //   setPageNumber(selectedPage);
  // };
  // //console.log(fileInfo.fileInfo)
  console.log(fileInfo.fileInfo[0])
  console.log(fileInfo.fileInfo[1])

  return (
    <>
      {/* <div>
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
      </div> */}
      <p className="pdf-current-page">
        Page {pageNumber || (numPages ? 1 : '--')} of {numPages || '--'}
      </p>
      <Document
        key={fileInfo.fileInfo[0]}
        file={fileInfo.fileInfo[0]}
        onLoadSuccess={onDocumentLoadSuccess}
        loading="잠시만 기다려 주세요."
        error="다시 시도해 주세요."
      >
        <Page pageNumber={pageNumber} width="700" />
      </Document>
    </>
  );
}

