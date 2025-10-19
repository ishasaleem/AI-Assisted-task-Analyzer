export default function TaskList({ title, tasks }) {
  return (
    <div className="p-4 bg-white rounded shadow-md mb-4">
      <h2 className="text-lg font-semibold mb-2">{title}</h2>
      <ul className="list-disc list-inside">
        {tasks.map((task, index) => (
          <li key={index} className="mb-1">{task}</li>
        ))}
      </ul>
    </div>
  );
}
