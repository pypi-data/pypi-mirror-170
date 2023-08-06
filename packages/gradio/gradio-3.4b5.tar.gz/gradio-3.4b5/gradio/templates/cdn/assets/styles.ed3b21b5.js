const get_style = (styles, key) => {
  return style_handlers[key](styles[key]);
};
function get_styles(styles, allowed_styles) {
  const processed_styles = allowed_styles.reduce((acc, next) => {
    if (styles[next] === void 0 || !style_handlers[next])
      acc[next] = " ";
    else {
      acc[next] = ` ${get_style(styles, next)} `;
    }
    return acc;
  }, {});
  processed_styles.classes = ` ${Object.values(processed_styles).join(" ").replace(/\s+/g, " ").trim()} `;
  return processed_styles;
}
const style_handlers = {
  container(container_visible) {
    return container_visible ? "" : `!p-0 !m-0 !border-0 !shadow-none !overflow-visible !bg-transparent`;
  },
  label_container(visible) {
    return visible ? "" : `!border-0 !shadow-none !overflow-visible !bg-transparent`;
  },
  grid(grid) {
    let grid_map = ["", "sm:", "md:", "lg:", "xl:", "2xl:"];
    let _grid = Array.isArray(grid) ? grid : [grid];
    return [0, 0, 0, 0, 0, 0].map((_, i) => `${grid_map[i]}grid-cols-${_grid?.[i] || _grid?.[_grid?.length - 1]}`).join(" ");
  },
  height(height) {
    return height === "auto" ? "auto" : "";
  },
  full_width(full_width) {
    return full_width ? "w-full grow" : "grow-0";
  },
  equal_height(equal_height) {
    return equal_height ? "items-stretch" : "unequal-height";
  },
  visible(visible) {
    return visible ? "" : "!hidden";
  },
  item_container(visible) {
    return visible ? "" : "!border-none";
  }
};
const create_classes = (styles, prefix = "") => {
  let classes = [];
  let target_styles = {};
  if (prefix === "") {
    target_styles = styles;
  } else {
    for (const prop in styles) {
      if (prop.startsWith(prefix + "_")) {
        const propname = prop.substring(prop.indexOf("_") + 1);
        target_styles[propname] = styles[prop];
      }
    }
  }
  if (target_styles.hasOwnProperty("margin")) {
    if (!Array.isArray(target_styles.margin)) {
      target_styles.margin = !!target_styles.margin ? [true, true, true, true] : [false, false, false, false];
    }
    let margin_map = ["t", "r", "b", "l"];
    target_styles.margin.forEach((margin, i) => {
      if (!margin) {
        classes.push(`!m${margin_map[i]}-0`);
      }
    });
  }
  if (target_styles.hasOwnProperty("border")) {
    if (!Array.isArray(target_styles.border)) {
      target_styles.border = !!target_styles.border ? [true, true, true, true] : [false, false, false, false];
    }
    let border_map = ["t", "r", "b", "l"];
    target_styles.border.forEach((border, i) => {
      if (!border) {
        classes.push(`!border-${border_map[i]}-0`);
      }
    });
  }
  switch (target_styles.rounded) {
    case true:
      classes.push("!rounded-lg");
      break;
    case false:
      classes.push("!rounded-none");
      break;
  }
  switch (target_styles.full_width) {
    case true:
      classes.push("w-full");
      break;
    case false:
      classes.push("!grow-0");
      break;
  }
  switch (target_styles.text_color) {
    case "red":
      classes.push("!text-red-500", "dark:text-red-100");
      break;
    case "yellow":
      classes.push("!text-yellow-500", "dark:text-yellow-100");
      break;
    case "green":
      classes.push("!text-green-500", "dark:text-green-100");
      break;
    case "blue":
      classes.push("!text-blue-500", "dark:text-blue-100");
      break;
    case "purple":
      classes.push("!text-purple-500", "dark:text-purple-100");
      break;
    case "black":
      classes.push("!text-gray-700", "dark:text-gray-50");
      break;
  }
  switch (target_styles.bg_color) {
    case "red":
      classes.push("!bg-red-100 !from-red-100 !to-red-200 !border-red-300", "dark:!bg-red-700 dark:!from-red-700 dark:!to-red-800 dark:!border-red-900");
      break;
    case "yellow":
      classes.push("!bg-yellow-100 !from-yellow-100 !to-yellow-200 !border-yellow-300", "dark:!bg-yellow-700 dark:!from-yellow-700 dark:!to-yellow-800 dark:!border-yellow-900");
      break;
    case "green":
      classes.push("!bg-green-100 !from-green-100 !to-green-200 !border-green-300", "dark:!bg-green-700 dark:!from-green-700 dark:!to-green-800 dark:!border-green-900  !text-gray-800");
      break;
    case "blue":
      classes.push("!bg-blue-100 !from-blue-100 !to-blue-200 !border-blue-300", "dark:!bg-blue-700 dark:!from-blue-700 dark:!to-blue-800 dark:!border-blue-900");
      break;
    case "purple":
      classes.push("!bg-purple-100 !from-purple-100 !to-purple-200 !border-purple-300", "dark:!bg-purple-700 dark:!from-purple-700 dark:!to-purple-800 dark:!border-purple-900");
      break;
    case "black":
      classes.push("!bg-gray-100 !from-gray-100 !to-gray-200 !border-gray-300", "dark:!bg-gray-700 dark:!from-gray-700 dark:!to-gray-800 dark:!border-gray-900");
    case "pink":
      classes.push("!bg-pink-100 !from-pink-100 !to-pink-200 !border-pink-300", "dark:!bg-pink-700 dark:!from-pink-700 dark:!to-pink-800 dark:!border-pink-900 !text-gray-800");
      break;
  }
  return " " + classes.join(" ");
};

export { create_classes as c, get_styles as g };
