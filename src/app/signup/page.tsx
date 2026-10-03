import Link from "next/link";
import { signIn } from "@/auth";

export default function SignupPage() {
    return (
        <main>
            <h1>Sign Up</h1>
            <p>Create a new Xenon Account</p>

            <form
                action={async () => {
                    "use server";
                    await signIn("keycloak", {
                        redirectTo: "/dashboard",
                        prompt: "create",
                    });
                }}
            >
                <button type="submit">Continue to Sign Up</button>
            </form>

            <p>
                Already have an account? <Link href="/login">Log In</Link>
            </p>
            <Link href="/">Back</Link>
        </main>
    );
}