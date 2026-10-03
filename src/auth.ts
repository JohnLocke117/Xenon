import NextAuth from "next-auth";
import Keycloak from "next-auth/providers/keycloak";
import { provisionUser } from "./lib/backend";

export const { handlers, auth, signIn, signOut } = NextAuth({
    providers: [Keycloak],
    session: {
        strategy: "jwt"
    },
    callbacks: {
        async signIn({ profile }) {
            if (!profile?.sub || !profile.email) {
                return false;
            }

            try {
                await provisionUser({
                    keycloak_subject: profile.sub,
                    email: profile.email,
                    name:
                        profile.name ??
                        [profile.given_name, profile.family_name].filter(Boolean).join(" ") ??
                        profile.email,
                });

                return true;
            } catch (error) {
                console.error("Account provisioning failed", error);
                return false;
            }
        }
    }
});