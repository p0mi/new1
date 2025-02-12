import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import Schedule from '/workspaces/new1/student-app/src/Schedule.tsx';
import Homeworks from '/workspaces/new1/student-app/src/Homeworks.tsx';
import FeedbackForm from '/workspaces/new1/student-app/src/FeedbackForm.tsx';
import './App.css'

const scheduleData = [
  { day: 'Понедельник', time: '9:00-10:30', subject: 'Математика' },
  { day: 'Вторник', time: '11:00-12:30', subject: 'Физика' },
  { day: 'Среда', time: '13:00-14:30', subject: 'История' },
];

const homeworksData = [
  { title: 'Домашнее задание по математике', description: 'Решить задачи на страницах 50-60 учебника.' },
  { title: 'Эссе по истории', description: 'Написать эссе на тему "Роль Петра I в истории России".' },
];

const App: React.FC = () => {
  return (
    <Container fluid>
      <Row>
        <Col md={8}>
          <h2>Расписание занятий</h2>
          <Schedule schedule={scheduleData} />
        </Col>
        <Col md={4}>
          <h2>Домашние задания</h2>
          <Homeworks homeworks={homeworksData} />
        </Col>
      </Row>
      <hr />
      <Row>
        <Col>
          <h2>Обратная связь</h2>
          <FeedbackForm />
        </Col>
      </Row>
    </Container>
  );
};

export default App;
