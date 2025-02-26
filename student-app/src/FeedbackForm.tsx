import React, { useState } from 'react';
import { Form, Button } from 'react-bootstrap';

const FeedbackForm: React.FC = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log({ name, email, message });
    alert('Спасибо за ваш отзыв!');
    setName('');
    setEmail('');
    setMessage('');
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group controlId="formBasicName">
        <Form.Label>Имя</Form.Label>
        <Form.Control type="text" value={name} onChange={(e) => setName(e.target.value)} required />
      </Form.Group>

      <Form.Group controlId="formBasicEmail">
        <Form.Label>Электронная почта</Form.Label>
        <Form.Control type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
      </Form.Group>

      <Form.Group controlId="formBasicMessage">
        <Form.Label>Сообщение</Form.Label>
        <Form.Control as="textarea" rows={3} value={message} onChange={(e) => setMessage(e.target.value)} required />
      </Form.Group>

      <Button variant="primary" type="submit">
        Отправить
      </Button>
    </Form>
  );
};

export default FeedbackForm;