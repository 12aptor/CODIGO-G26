import { InputHTMLAttributes } from "react";
import { cn } from "../../lib/utils";

interface IProps extends InputHTMLAttributes<HTMLInputElement> {
  className: string;
  type: string;
}

export const Input = ({ className, type, ...props }: IProps) => {
  return (
    <input
      type={type}
      className={cn(
        "flex w-full h-9 rounded-md border border-gray-800 bg-transparent px-3 py-1 text-sm shadow-sm outline-none",
        className
      )}
      {...props}
    />
  );
};
