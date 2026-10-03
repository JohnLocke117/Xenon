"use client"

import Link from "next/link"

import { FormEvent, useState } from "react";

export default function SignupPage() {
    const [message, setMessage] = useState("");

    function handleSubmit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault();
        setMessage("Signup is a Placeholder");
    }

    return (
        <main>
            <h1>Sign Up</h1>
            <p>Create your Xenon Account</p>

            <form onSubmit={handleSubmit}>
                <label htmlFor="name">Name</label>
                <input
                    id="name"
                    name="Name"
                    type="text"
                    autoComplete="name"
                    required
                />

                <br />

                <label htmlFor="email">Email</label>
                <input
                    id="email"
                    name="email"
                    type="email"
                    autoComplete="email"
                    required
                />

                <br />

                <label htmlFor="password">Passowrd</label>
                <input
                    id="passowrd"
                    name="password"
                    type="password"
                    autoComplete="new-password"
                    required
                    minLength={6}
                />

                <br />

                <button type="submit">Create Account</button>
            </form>

            {message && <p role="status">{message}</p>}

            <p>
                Already have an Account? <Link href="/login">Log In</Link>
            </p>

            <Link href="/">Back</Link>
        </main>
    );
}