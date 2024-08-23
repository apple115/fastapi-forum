import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Header from "@/components/Header";
import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Siderbar";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "forum",
  description: "fastapi-forum-frontend",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Header />
        <Navbar />
        <div className="flex h-screen">
          <Sidebar />
          <div className="flex-grow p-4">{children}</div>
        </div>
      </body>
    </html>
  );
}
