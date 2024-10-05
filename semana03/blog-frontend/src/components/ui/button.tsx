import { ButtonHTMLAttributes } from "react";
import { cn } from "../../lib/utils";

interface IProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  className: string;
}

export const Button = ({ className, ...props }: IProps) => {
  return (
    <button
      className={cn(
        "h-9 inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium bg-black shadow text-white",
        className
      )}
      {...props}
    />
  );
};
