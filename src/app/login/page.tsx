"use client"

import Link from "next/link";
import { FormEvent, useState } from "react"


export default function LoginPage() {
    const [message, setMessage] = useState("")

    function handleSumbit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault()
    }

    setMessage("Login is Placeholder right now");

    return (
        <main>
            <h1>Log In</h1>
            <p>Welcome back to Xenon</p>

            <form onSubmit={handleSumbit}>
                <label htmlFor="email">Email</label>
                <input
                    id="email"
                    name="email"
                    type="email"
                    autoComplete="email"
                    required
                />

                <label htmlFor="password"></label>
                <input 
                    id="password"
                    name="password"
                    type="password"
                    autoComplete="current-password"
                    required
                />

                <button type="submit">Log In</button>
            </form>

            {message && <p role="status">{message}</p>}

            <p>
                Don't have an Account? <Link href="/signup">Sign Up</Link>
            </p>

            <Link href="/">Back</Link>
        </main>
    );
}