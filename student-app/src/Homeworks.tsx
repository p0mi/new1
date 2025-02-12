import React from 'react';
import { ListGroup } from 'react-bootstrap';

interface HomeworkProps {
  homeworks: Array<{ title: string; description: string }>;
}

const Homeworks: React.FC<HomeworkProps> = ({ homeworks }) => {
  return (
    <ListGroup>
      {homeworks.map((hw, index) => (
        <ListGroup.Item key={index}>
          <h5>{hw.title}</h5>
          <p>{hw.description}</p>
        </ListGroup.Item>
      ))}
    </ListGroup>
  );
};

export default Homeworks;