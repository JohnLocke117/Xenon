import Link from "next/link";

export default function Home() {
    return (
        <main>
            <h1>Hello, Xenon!</h1>
            <button type="button">
                <Link href="/signup">Sign Up</Link>
            </button>
            <button type="button">
                <Link href="/login">Login</Link>
            </button>
        </main>
    );
}
