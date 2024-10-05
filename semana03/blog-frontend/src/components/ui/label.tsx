import { HTMLAttributes } from "react";

interface IProps extends HTMLAttributes<HTMLLabelElement> {
  htmlFor: string;
}

export const Label = ({ htmlFor, ...props }: IProps) => {
  return (
    <label
      className="text-sm font-medium leading-none"
      htmlFor={htmlFor}
      {...props}
    />
  );
};
