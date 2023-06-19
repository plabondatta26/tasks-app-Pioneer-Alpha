import React from "react";
import { useAppDispatch } from "../../../store/hooks";
import { tasksActions } from "../../../store/Tasks.store";
import { ReactComponent as StarLine } from "../../../assets/star-line.svg";

const BtnMarkAsImportant: React.FC<{
  taskId: string;
  taskImportant: boolean;
}> = ({ taskId, taskImportant }) => {
  const dispatch = useAppDispatch();

  const markAsImportantHandler = () => {
    fetch(`http://localhost:8000/api/edit/task/status/${taskId}?is_important=${taskImportant}&status=important`)
    .then(response => {
      return Promise.all([response.status, response.json()]);
    })
    .then(([code, data])=> {
      if (code === 200) {
        dispatch(tasksActions.markAsImportant(taskId));
      }
      alert(data?.details);
    })
    .catch(err=> {
      alert(err?.message);
    });
  };

  return (
    <button
      title={taskImportant ? "unmark as important" : "mark as important"}
      onClick={markAsImportantHandler}
      className="transition hover:text-slate-700 dark:hover:text-slate-200 ml-auto"
    >
      <StarLine
        className={`w-5 h-5 sm:w-6 sm:h-6 ${
          taskImportant ? "fill-rose-500 stroke-rose-500 " : "fill-none"
        }`}
      />
    </button>
  );
};

export default React.memo(BtnMarkAsImportant);
