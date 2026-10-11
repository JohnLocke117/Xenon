import type { DefaultSession } from "next-auth";
import { XenonUser } from "./xenon";

declare module "next-auth" {
    interface Session {
        user: DefaultSession["user"] & {
            xenon?: XenonUser;
        };
    }
}

declare module "next-auth/jwt" {
    interface JWT {
        xenonUser?: XenonUser;
        idToken?: string;
    }
}
