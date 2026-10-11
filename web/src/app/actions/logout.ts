"use server";

import { headers } from "next/headers";
import { signOut } from "@/auth";
import { getToken } from "next-auth/jwt";
import { redirect } from "next/navigation";

function requiredEnv(name: string): string {
    const value = process.env[name];
    if (!value) throw new Error(`Missing environment variable: ${name}`);
    return value;
}

export async function logout(): Promise<void> {
    const appUrl = new URL(requiredEnv("AUTH_URL"));
    const issuer = requiredEnv("AUTH_KEYCLOAK_ISSUER").replace(/\/+$/, "");
    const clientId = requiredEnv("AUTH_KEYCLOAK_ID");

    // Read the token before signOut clears the session cookie
    const token = await getToken({
        req: { headers: new Headers(await headers()) },
        secret: requiredEnv("AUTH_SECRET"),
        secureCookie: appUrl.protocol === "https:",
    });

    const logoutUrl = new URL(`${issuer}/protocol/openid-connect/logout`);

    logoutUrl.searchParams.set("client_id", clientId);
    logoutUrl.searchParams.set(
        "post_logout_redirect_uri",
        new URL("/", appUrl).toString()
    );

    if (token?.idToken) {
        logoutUrl.searchParams.set("id_token_hint", token.idToken);
    }

    // Clear the local session without immediately redirecting home
    await signOut({ redirect: false, redirectTo: "/" });

    // The browser must visit Keycloak to end its SSO session
    redirect(logoutUrl.toString());
}
