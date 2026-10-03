import { redirect } from "next/navigation";
import { auth, signOut } from "@/auth";

export default async function DashboardPage() {
    const session = await auth();

    if (!session?.user) {
        redirect("/login");
    }

    return (
        <main>
            <h1>Hello {session.user.name ?? session.user.email ?? "there"}!</h1>
            <p>Welcome to your Xenon Dashboard.</p>

            <form
                action={async () => {
                    "use server";
                    await signOut({  redirectTo: "/"});
                }}
            >
                <button type="submit">Log Out</button>
            </form>
        </main>
    )
}