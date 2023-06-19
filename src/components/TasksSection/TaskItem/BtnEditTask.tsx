import React, { useState } from "react";
import { useAppDispatch } from "../../../store/hooks";
import { tasksActions } from "../../../store/Tasks.store";
import ModalCreateTask from "../../Utilities/ModalTask";
import { ReactComponent as OptionsSvg } from "../../../assets/options.svg";
import { Task } from "../../../interfaces";

const BtnEditTask: React.FC<{ task: Task }> = ({ task }) => {
  const [modalEditTaskOpen, setModalEditTaskOpen] = useState<boolean>(false);
  const dispatch = useAppDispatch();

  const closeModalEditTask = () => {
    setModalEditTaskOpen(false);
  };

  const openModalEditTask = () => {
    setModalEditTaskOpen(true);
  };

  const editTaskHandler = (task: Task) => {
    const payload = {
      method: 'PUT',
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
    fetch(`http://localhost:8000/api/edit/task/${task.id}/`, payload)
    .then(response => {
      return Promise.all([response.status, response.json()]);
    })
    .then(([code, data])=> {
      if (code === 200) {
        const updatedTask: Task = {
          id: data?.id,
          title: data?.title,
          dir: data?.directory?.title,
          description: data?.description,
          date: data?.date,
          important: data?.is_important,
          completed: data?.is_completed
        };
        
       dispatch(tasksActions.editTask(updatedTask));
      }
     alert(data.details);
  })
  .catch(err => {
    alert(err.message);
  })
  };

  return (
    <>
      <button
        title="edit task"
        className="transition w-7 sm:w-8 h-6 sm:h-8 grid place-items-center dark:hover:text-slate-200 hover:text-slate-700"
        onClick={openModalEditTask}
      >
        <OptionsSvg className="w-4 sm:w-5 h-4 sm:h-5" />
      </button>
      {modalEditTaskOpen && (
        <ModalCreateTask
          onClose={closeModalEditTask}
          task={task}
          nameForm="Edit task"
          onConfirm={editTaskHandler}
        />
      )}
    </>
  );
};

export default BtnEditTask;
