export interface LoginRequest {
  email: string;
  password: string;
}

export interface LoginResponse {
  access_token: string;
  token_type: string;
}

export interface RegisterRequest {
  name: string;
  email: string;
  password: string;
  default_email: string | null;
  default_phone: string | null;
}

export interface RegisterResponse {
  id: string;
  name: string;
  email: string;
  default_email: string | null;
  default_phone: string | null;
}