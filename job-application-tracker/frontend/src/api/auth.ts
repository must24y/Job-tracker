import apiClient from "./client";

import type {
  LoginRequest,
  LoginResponse,
  RegisterRequest,
  RegisterResponse,
} from "../types/auth";

export async function loginUser(
  payload: LoginRequest,
): Promise<LoginResponse> {
  return apiClient<LoginResponse>(
    "/auth/login",
    {
      method: "POST",
      body: JSON.stringify(payload),
    },
  );
}

export async function registerUser(
  payload: RegisterRequest,
): Promise<RegisterResponse> {
  return apiClient<RegisterResponse>(
    "/auth/register",
    {
      method: "POST",
      body: JSON.stringify(payload),
    },
  );
}