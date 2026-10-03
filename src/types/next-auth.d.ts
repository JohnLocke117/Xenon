import type { DefaultSession } from "next-auth";

type XenonUser = {
    user_id: string;
    email: string;
    name: string;
    role: "basic" | "admin";
};

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
    }
}
