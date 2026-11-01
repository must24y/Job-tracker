import { StrictMode, useEffect, useState } from "react";
import { createRoot } from "react-dom/client";

type PageInfo = {
  title: string;
  url: string;
};

function ExtensionApp() {
  const [pageInfo, setPageInfo] = useState<PageInfo | null>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    async function getCurrentPageInfo() {
      try {
        const tabs = await chrome.tabs.query({
          active: true,
          currentWindow: true,
        });

        const activeTab = tabs[0];

        if (!activeTab?.id) {
          setError("Could not identify the current tab.");
          return;
        }

        const response = await chrome.tabs.sendMessage(
          activeTab.id,
          {
            type: "GET_PAGE_INFO",
          },
        );

        setPageInfo(response);
      } catch {
        setError(
          "Could not retrieve page information. Try refreshing the website.",
        );
      }
    }

    getCurrentPageInfo();
  }, []);

  return (
    <main className="min-h-screen w-full bg-white p-5 text-gray-900">
      <header className="mb-6">
        <h1 className="text-2xl font-bold">Job Tracker</h1>

        <p className="mt-1 text-sm text-gray-500">
          Save and manage job applications.
        </p>
      </header>

      <section className="rounded-lg border border-gray-200 p-4">
        <h2 className="text-lg font-semibold">Current page</h2>

        {pageInfo && (
          <div className="mt-3 space-y-2">
            <div>
              <p className="text-xs font-medium text-gray-500">
                Page title
              </p>

              <p className="text-sm">{pageInfo.title}</p>
            </div>

            <div>
              <p className="text-xs font-medium text-gray-500">
                Page URL
              </p>

              <p className="break-all text-sm">{pageInfo.url}</p>
            </div>
          </div>
        )}

        {error && (
          <p className="mt-3 text-sm text-red-600">
            {error}
          </p>
        )}
      </section>
    </main>
  );
}

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <ExtensionApp />
  </StrictMode>,
);