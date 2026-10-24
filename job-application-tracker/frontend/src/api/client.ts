const API_BASE_URL = "YOUR_BACKEND_URL";

type RequestOptions = RequestInit & {
  requiresAuth?: boolean;
};

async function apiClient<T>(
  endpoint: string,
  options: RequestOptions = {},
): Promise<T> {
  const { requiresAuth = false, ...fetchOptions } = options;

  const token = localStorage.getItem("access_token");

  const headers = new Headers(fetchOptions.headers);

  headers.set("Content-Type", "application/json");
  headers.set("Accept", "application/json");

  if (requiresAuth && token) {
    headers.set("Authorization", `Bearer ${token}`);
  }

  const response = await fetch(
    `${API_BASE_URL}${endpoint}`,
    {
      ...fetchOptions,
      headers,
    },
  );

  if (!response.ok) {
    const errorData = await response.json().catch(() => null);

    throw new Error(
      errorData?.detail || "Something went wrong",
    );
  }

  return response.json() as Promise<T>;
}

export default apiClient;