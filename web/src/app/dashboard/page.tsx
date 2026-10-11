import { redirect } from "next/navigation";
import { auth } from "@/auth";
import { logout } from "@/app/actions/logout";

export default async function DashboardPage() {
    const session = await auth();

    if (!session?.user) {
        redirect("/login");
    }

    const name = session.user.xenon?.name ?? session.user.name ?? "there";

    return (
        <main>
            <h1>Hello {name}!</h1>
            <p>Welcome to your Xenon Dashboard.</p>

            <p>Role: {session.user.xenon?.role ?? "unknown"}</p>

            <form action={logout}>
                <button type="submit">Log Out</button>
            </form>
        </main>
    );
}
