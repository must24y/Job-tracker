import { useState } from "react";
import { NavLink } from "react-router-dom";

import {
  LayoutDashboard,
  Briefcase,
  Bookmark,
  User,
  Menu,
} from "lucide-react";

const menuItems = [
  {
    label: "Dashboard",
    icon: LayoutDashboard,
    path: "/dashboard",
  },
  {
    label: "Applications",
    icon: Briefcase,
    path: "/applications",
  },
  {
    label: "Saved Jobs",
    icon: Bookmark,
    path: "/saved-jobs",
  },
  {
    label: "Profile",
    icon: User,
    path: "/profile",
  },
];

function Sidebar() {
  const [isOpen, setIsOpen] = useState(true);

  return (
    <aside
      className={`min-h-screen bg-slate-900 text-white transition-all duration-300 ${
        isOpen ? "w-64" : "w-20"
      }`}
    >
      {/* Header */}
      <div className="flex items-center justify-between p-6">
        {isOpen && (
          <h1 className="text-2xl font-bold">
            JobTracker
          </h1>
        )}

        <button
          onClick={() => setIsOpen(!isOpen)}
          className="rounded-lg p-2 hover:bg-slate-800"
        >
          <Menu size={22} />
        </button>
      </div>

      {/* Navigation */}
      <nav className="px-4">
        {menuItems.map((item) => {
          const Icon = item.icon;

          return (
            <NavLink
              key={item.label}
              to={item.path}
              className={({ isActive }) =>
                `mb-2 flex items-center gap-3 rounded-lg px-4 py-3 transition-colors ${
                  isActive
                    ? "bg-slate-800 text-white"
                    : "text-slate-300 hover:bg-slate-800 hover:text-white"
                }`
              }
            >
              <Icon size={20} />

              {isOpen && (
                <span>{item.label}</span>
              )}
            </NavLink>
          );
        })}
      </nav>
    </aside>
  );
}

export default Sidebar;