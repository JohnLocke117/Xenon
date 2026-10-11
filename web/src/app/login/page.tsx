import { signIn } from "@/auth";
import Link from "next/link";

export default function LoginPage() {
    return (
        <main>
            <h1>Log In</h1>
            <p>Welcome back to Xenon</p>

            <form
                action={async () => {
                    "use server";
                    await signIn("keycloak", {
                        redirectTo: "/dashboard",
                    });
                }}
            >
                <button type="submit">Continue to Log In</button>
            </form>

            <p>
                Don&apos;t have an account? <Link href="/signup">Sign Up</Link>
            </p>

            <Link href="/">Back</Link>
        </main>
    );
}
