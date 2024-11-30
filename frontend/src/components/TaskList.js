import React from 'react';
import axios from 'axios';

const TaskList = ({ tasks, fetchTasks }) => {
  const handleDelete = async (id) => {
    await axios.delete(`http://localhost:8000//api/todos/${id}/`);
    fetchTasks();
  };

  const handleToggle = async (id, completed) => {
    await axios.put(`http://localhost:8000//api/todos/${id}/`, { completed: !completed });
    fetchTasks();
  };

  return (
    <ul>
      {tasks.map(task => (
        <li key={task.id}>
          <input 
            type="checkbox" 
            checked={task.completed} 
            onChange={() => handleToggle(task.id, task.completed)} 
          />
          {task.title}
          <button onClick={() => handleDelete(task.id)}>Delete</button>
        </li>
      ))}
    </ul>
  );
};

export default TaskList;
