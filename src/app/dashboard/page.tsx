"use client"

import Link from "next/link"
import { useState } from "react"

export default function DashboardPage() {
    const [loggedOut, setLoggedOut] = useState(false);

    function handleLogout() {
        setLoggedOut(true);
    }

    if (loggedOut) {
        return (
            <main>
                <p>You have logged out</p>
                <Link href="/">Back to Home</Link>
            </main>
        );
    }

    const name = "Lorem Ipsum"

    return (
        <main>
            <h1>Hello {name}!</h1>
            <p>Welcome to Xenon Dashboard</p>

            <button type="button" onClick={handleLogout}>Log Out</button>
        </main>
    );
}