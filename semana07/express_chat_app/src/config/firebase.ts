import { initializeApp } from "firebase/app";
import dotenv from "dotenv";

dotenv.config();

const firebaseConfig = {
  apiKey: process.env.FIREBASE_API_KEY,
  authDomain: "chat-app-f578b.firebaseapp.com",
  projectId: "chat-app-f578b",
  storageBucket: "chat-app-f578b.appspot.com",
  messagingSenderId: "1075814344566",
  appId: "1:1075814344566:web:896ca8cc3b23d194a57c57"
};

export const firebaseApp = initializeApp(firebaseConfig);