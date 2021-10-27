import React from 'react';

import { Formik } from 'formik';
import { Button, Col, Form, Row } from 'react-bootstrap';

function Search ({ search }) {
  const onSubmit = async (values, actions) => {
    await search(
      values.query
    );
  };

  return (
    <Formik
      initialValues={{
        query: '',
      }}
      onSubmit={onSubmit}
    >
      {({
        handleChange,
        handleSubmit,
        values
      }) => (
        <Form noValidate onSubmit={handleSubmit}>
          <Form.Group controlId='query'>
            <Form.Label>Query</Form.Label>
            <Col>
              <Form.Control
                type='text'
                name='query'
                placeholder='Enter a search term (e.g. Chanel)'
                value={values.query}
                onChange={handleChange}
              />
              <Form.Text className='text-muted'>
                Searches for query in text body.
              </Form.Text>
            </Col>
          </Form.Group>
          <Form.Group as={Row}>
            <Col>
              <Button type='submit' variant='primary'>Search</Button>
            </Col>
          </Form.Group>
        </Form>
      )}
    </Formik>
  );
}

export default Search;