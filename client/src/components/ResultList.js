import React from 'react';

import { sanitize } from 'dompurify'; // new
import { Card } from 'react-bootstrap'; // new

function ResultList ({ results }) {
  const resultItems = results.map(result =>
    <Card className='mb-3' key={result.id}>
      <Card.Body>
        {/*<Card.Title*/}
        {/*  dangerouslySetInnerHTML={{*/}
        {/*    __html: `${sanitize(result.text)}`*/}
        {/*  }}*/}
        {/*></Card.Title>*/}
        <Card.Text dangerouslySetInnerHTML={{ __html: sanitize(result.text) }} />
      </Card.Body>
    </Card>
  );

  return (
    <div>
      {!results && <p>Search using the left panel.</p>}
      {results && results.length === 0 && <p>No results found.</p>}
      {resultItems}
    </div>
  );
}

export default ResultList;