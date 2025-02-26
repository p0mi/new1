import React from 'react';
import { Table } from 'react-bootstrap';

interface ScheduleProps {
  schedule: Array<{ day: string; time: string; subject: string }>;
}

const Schedule: React.FC<ScheduleProps> = ({ schedule }) => {
  return (
    <Table striped bordered hover>
      <thead>
        <tr>
          <th>День недели</th>
          <th>Время</th>
          <th>Предмет</th>
        </tr>
      </thead>
      <tbody>
        {schedule.map((item, index) => (
          <tr key={index}>
            <td>{item.day}</td>
            <td>{item.time}</td>
            <td>{item.subject}</td>
          </tr>
        ))}
      </tbody>
    </Table>
  );
};

export default Schedule;