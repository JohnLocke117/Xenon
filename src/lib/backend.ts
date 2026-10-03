function requiredEnv(name: string): string {
    const value = process.env[name];

    if (!value) {
        throw new Error(`Missing required environment variable: ${name}`);
    }

    return value;
}

const backendUrl = requiredEnv("BACKEND_INTERNAL_URL");
const bffServiceToken = requiredEnv("BFF_SERVICE_TOKEN");

if (!backendUrl || !bffServiceToken) {
    throw new Error("Missing backend BFF Configuration");
}

export async function provisionUser(identity: {
    keycloak_subject: string;
    email: string;
    name: string;
}) {
    const response = await fetch(`${backendUrl}/auth/provision`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-BFF-Service-Token": bffServiceToken
        },
        body: JSON.stringify(identity),
        cache: "no-store"
    });

    if (!response.ok) {
        throw new Error(`User provisioning failed (${response.status})`);
    }

    return response.json() as Promise<{
        user_id: string;
        email: string;
        name: string;
        role: "basic" | "admin";
    }>;
}