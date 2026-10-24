import { Bell } from "lucide-react";

function Topbar() {
  return (
    <header className="flex h-16 items-center justify-between border-b bg-white px-8">
      <div>
        <h2 className="text-xl font-semibold text-slate-800">
          Dashboard
        </h2>
      </div>

      <div className="flex items-center gap-4">
        <button className="rounded-full p-2 text-slate-600 hover:bg-slate-100">
          <Bell size={20} />
        </button>

        <div className="flex h-9 w-9 items-center justify-center rounded-full bg-slate-200 font-semibold text-slate-700">
          M
        </div>
      </div>
    </header>
  );
}

export default Topbar;