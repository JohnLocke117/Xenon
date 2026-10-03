import NextAuth from "next-auth";
import Keycloak from "next-auth/providers/keycloak";
import { provisionUser } from "./lib/backend";

const keycloakProvider = Keycloak;

const keycloakRegistrationProvider = Keycloak({
    id: "keycloak-registration",
    authorization: {
        params: {
            prompt: "create",
        }
    }
});

export const { handlers, auth, signIn, signOut } = NextAuth({
    providers: [keycloakProvider, keycloakRegistrationProvider],

    session: {
        strategy: "jwt"
    },

    callbacks: {
        async signIn({ profile }) {
            return Boolean(profile?.sub && profile.email);
        },

        async jwt({ token, account, profile }) {
            // Account is present on the initial OIDC Callback, not on later session reads
            if (
                account?.provider === "keycloak" ||
                account?.provider === "keycloak-registration"
            ) {
                if (!profile?.sub || !profile.email) {
                    throw new Error("Keycloak profile is missing required identity claims");
                }

                const profileName =
                    profile.name?.trim() ||
                    [profile.given_name, profile.family_name].filter(Boolean).join(" ").trim() ||
                    profile.email;
                
                const xenonUser = await provisionUser({
                    keycloak_subject: profile.sub,
                    email: profile.email,
                    name: profileName,
                });

                token.xenonUser = xenonUser;
            }

            return token;
        },

        async session({ session, token }) {
            if (session.user && token.xenonUser) {
                session.user.xenon = token.xenonUser;
            }

            return session;
        }
    }
});