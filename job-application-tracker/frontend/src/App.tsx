import { BrowserRouter, Routes, Route } from "react-router-dom";

import Sidebar from "./components/Sidebar";
import Topbar from "./components/Topbar";

import Dashboard from "./pages/Dashboard";
import Applications from "./pages/Applications";
import SavedJobs from "./pages/SavedJobs";
import Profile from "./pages/Profile";

function App() {
  return (
    <BrowserRouter>
      <div className="flex min-h-screen">
        <Sidebar />

        <div className="flex flex-1 flex-col">
          <Topbar />

          <main className="flex-1 bg-slate-50 p-8">
            <Routes>
              <Route
                path="/dashboard"
                element={<Dashboard />}
              />

              <Route
                path="/applications"
                element={<Applications />}
              />

              <Route
                path="/saved-jobs"
                element={<SavedJobs />}
              />

              <Route
                path="/profile"
                element={<Profile />}
              />
            </Routes>
          </main>
        </div>
      </div>
    </BrowserRouter>
  );
}

export default App;