export interface ICredentials {
  email: string;
  password: string;
}

export interface IRegisterUser {
  name: string;
  email: string;
  password: string;
  status: boolean;
}

export interface IPost {
  readonly id: number;
  title: string;
  content: string;
  image: string;
  created_at: string;
  updated_at: string;
  author_id: number;
  author: {
    id: number;
    name: string;
    email: string;
    status: boolean;
    created_at: string;
    updated_at: string;
  };
}
