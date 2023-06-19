import React from "react";
import { useAppDispatch } from "../../../store/hooks";
import { tasksActions } from "../../../store/Tasks.store";
import { ReactComponent as SvgX } from "../../../assets/x.svg";
import { ReactComponent as Check } from "../../../assets/check.svg";

const BtnToggleCompleted: React.FC<{
  taskCompleted: boolean;
  taskId: string;
  isListInView1: boolean;
}> = ({ taskCompleted, taskId, isListInView1 }) => {
  const dispatch = useAppDispatch();

  const toggleTaskCompleted = (id: string) => {

    fetch(`http://localhost:8000/api/edit/task/status/${id}/?is_completed=${taskCompleted}&status=completed`)
    .then(response =>{
      return Promise.all([response.status, response.json()]);
    })
    .then(([code, data])=> {
      if (code === 200) {
        dispatch(tasksActions.toggleTaskCompleted(id));
      }
      alert(data?.details);
    })
    .catch(err=> {
      alert(err?.message);
    });
  };

  return (
    <button
      title={taskCompleted ? "mark as uncompleted" : "mark as completed"}
      className={`${
        taskCompleted
          ? "bg-emerald-200 text-emerald-800 "
          : "bg-amber-200 text-amber-800 "
      } ${isListInView1 ? "mr-4" : "mr-4 order-0"} rounded-full font-medium`}
      onClick={() => toggleTaskCompleted(taskId)}
    >
      <span className="block py-1 px-3 absolute invisible sm:static sm:visible">
        {taskCompleted ? "completed" : "uncompleted"}
      </span>
      <span className=" sm:hidden w-6 h-6 grid place-items-center">
        {taskCompleted ? (
          <Check className="w-3 h-3" />
        ) : (
          <SvgX className="w-3 h-3" />
        )}
      </span>
    </button>
  );
};

export default React.memo(BtnToggleCompleted);
