import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Maestro Español MX",
  description:
    "Translate English phrases into Mexican Spanish and generate AI-powered practice materials."
};

export default function RootLayout({
  children
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
