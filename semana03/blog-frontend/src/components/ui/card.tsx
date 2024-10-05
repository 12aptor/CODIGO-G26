import { HTMLAttributes } from "react";
import { cn } from "../../lib/utils";

interface IProps extends HTMLAttributes<HTMLDivElement> {
  className: string;
}

export const Card = ({ className, ...props }: IProps) => {
  return (
    <div
      className={cn("rounded-lg border bg-white shadow", className)}
      {...props}
    />
  );
};
