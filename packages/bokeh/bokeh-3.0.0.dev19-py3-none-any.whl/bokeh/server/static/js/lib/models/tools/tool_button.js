import Hammer from "hammerjs";
import { DOMElementView } from "../../core/dom_view";
import { div, empty } from "../../core/dom";
import { ToolIcon } from "../../core/enums";
import { ContextMenu } from "../../core/util/menus";
import { reversed } from "../../core/util/array";
import tools_css, * as tools from "../../styles/tool_button.css";
import icons_css, * as icons from "../../styles/icons.css";
export class ToolButtonView extends DOMElementView {
    initialize() {
        super.initialize();
        const items = this.model.menu;
        if (items == null) {
            this.el.addEventListener("click", (e) => {
                if (e.composedPath().includes(this.el)) {
                    this._clicked();
                }
            });
        }
        else {
            const { location } = this.parent.model;
            const reverse = location == "left" || location == "above";
            const orientation = this.parent.model.horizontal ? "vertical" : "horizontal";
            this._menu = new ContextMenu(!reverse ? items : reversed(items), {
                target: this.root.el,
                orientation,
                prevent_hide: (event) => event.composedPath().includes(this.el),
            });
            this._hammer = new Hammer(this.el, {
                cssProps: {},
                touchAction: "auto",
                inputClass: Hammer.TouchMouseInput, // https://github.com/bokeh/bokeh/issues/9187
            });
            this._hammer.on("tap", (e) => {
                const { _menu } = this;
                if (_menu != null && _menu.is_open) {
                    _menu.hide();
                    return;
                }
                if (e.srcEvent.composedPath().includes(this.el)) {
                    this._clicked();
                }
            });
            this._hammer.on("press", () => this._pressed());
            this.el.addEventListener("keydown", (event) => {
                if (event.key == "Enter") {
                    this._clicked();
                }
            });
        }
    }
    connect_signals() {
        this.connect(this.model.change, () => this.render());
    }
    remove() {
        this._hammer?.destroy();
        this._menu?.remove();
        super.remove();
    }
    styles() {
        return [...super.styles(), tools_css, icons_css];
    }
    css_classes() {
        return super.css_classes().concat(tools.tool_button);
    }
    render() {
        empty(this.el);
        const icon_el = div({ class: tools.tool_icon });
        this.el.appendChild(icon_el);
        if (this.model.menu != null) {
            const icon = (() => {
                switch (this.parent.model.location) {
                    case "above": return icons.tool_icon_chevron_down;
                    case "below": return icons.tool_icon_chevron_up;
                    case "left": return icons.tool_icon_chevron_right;
                    case "right": return icons.tool_icon_chevron_left;
                }
            })();
            const chevron_el = div({ class: [tools.tool_chevron, icon] });
            this.el.appendChild(chevron_el);
        }
        const icon = this.model.computed_icon;
        if (icon != null) {
            if (icon.startsWith("data:image")) {
                const url = `url("${encodeURI(icon)}")`;
                icon_el.style.backgroundImage = url;
            }
            else if (icon.startsWith("--")) {
                icon_el.style.backgroundImage = `var(${icon})`;
            }
            else if (icon.startsWith(".")) {
                const cls = icon.substring(1);
                icon_el.classList.add(cls);
            }
            else if (ToolIcon.valid(icon)) {
                const cls = `bk-tool-icon-${icon.replace(/_/g, "-")}`;
                icon_el.classList.add(cls);
            }
        }
        this.el.title = this.model.tooltip;
        this.el.tabIndex = 0;
    }
    _pressed() {
        const at = (() => {
            switch (this.parent.model.location) {
                case "right": return { left_of: this.el };
                case "left": return { right_of: this.el };
                case "above": return { below: this.el };
                case "below": return { above: this.el };
            }
        })();
        this._menu?.toggle(at);
    }
}
ToolButtonView.__name__ = "ToolButtonView";
//# sourceMappingURL=tool_button.js.map