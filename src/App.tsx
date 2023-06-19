import React from "react";
import AccountData from "./components/AccountSection/AccountData";
import Footer from "./components/Footer";
import Menu from "./components/Menu/Menu";
import TasksSection from "./components/TasksSection/TasksSection";
import ModalCreateTask from "./components/Utilities/ModalTask";
import { Task } from "./interfaces";
import { useAppDispatch, useAppSelector } from "./store/hooks";
import { modalActions } from "./store/Modal.store";
import { tasksActions } from "./store/Tasks.store";

const App: React.FC = () => {
  const modal = useAppSelector((state) => state.modal);

  const dispatch = useAppDispatch();

  const closeModalCreateTask = () => {
    dispatch(modalActions.closeModalCreateTask());
  };

  const createNewTaskHandler = (task: Task) => {
    const payload = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        title: task.title,
        directory: task.dir,
        description: task.description,
        date: task.date,
        is_important: task.important,
        is_completed: task.completed
      })
    };
    fetch('http://localhost:8000/api/create/task/', payload)
    .then(response => {
      return Promise.all([response.status, response.json()]);
    })
    .then(([code, data])=> {
      if (code === 201){
        const updatedTask: Task = {
          id: data?.id,
          title: data?.title,
          dir: data?.directory?.title,
          description: data?.description,
          date: data?.date,
          important: data?.is_important,
          completed: data?.is_completed
        };
        dispatch(tasksActions.addNewTask(updatedTask));
      }
      alert(data?.details)
  })
  .catch(err => {
   alert(err.message)
  })
  };

  return (
    <div className="bg-slate-200 min-h-screen text-slate-600 dark:bg-slate-900 dark:text-slate-400 xl:text-base sm:text-sm text-xs">
      {modal.modalCreateTaskOpen && (
        <ModalCreateTask
          onClose={closeModalCreateTask}
          nameForm="Add a task"
          onConfirm={createNewTaskHandler}
        />
      )}
      <Menu />
      <TasksSection />
      <Footer />
      <AccountData />
    </div>
  );
};

export default App;
