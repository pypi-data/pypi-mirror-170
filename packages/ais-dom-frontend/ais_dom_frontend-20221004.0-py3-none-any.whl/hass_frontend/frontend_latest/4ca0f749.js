/*! For license information please see 4ca0f749.js.LICENSE.txt */
"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[34377],{54040:(t,e,i)=>{var o=i(87480),r=i(33310),n=i(58417),a=i(39274);let l=class extends n.A{};l.styles=[a.W],l=(0,o.__decorate)([(0,r.Mo)("mwc-checkbox")],l)},92685:(t,e,i)=>{i.d(e,{a:()=>m});var o=i(87480),r=i(72774),n={ROOT:"mdc-form-field"},a={LABEL_SELECTOR:".mdc-form-field > label"};const l=function(t){function e(i){var r=t.call(this,(0,o.__assign)((0,o.__assign)({},e.defaultAdapter),i))||this;return r.click=function(){r.handleClick()},r}return(0,o.__extends)(e,t),Object.defineProperty(e,"cssClasses",{get:function(){return n},enumerable:!1,configurable:!0}),Object.defineProperty(e,"strings",{get:function(){return a},enumerable:!1,configurable:!0}),Object.defineProperty(e,"defaultAdapter",{get:function(){return{activateInputRipple:function(){},deactivateInputRipple:function(){},deregisterInteractionHandler:function(){},registerInteractionHandler:function(){}}},enumerable:!1,configurable:!0}),e.prototype.init=function(){this.adapter.registerInteractionHandler("click",this.click)},e.prototype.destroy=function(){this.adapter.deregisterInteractionHandler("click",this.click)},e.prototype.handleClick=function(){var t=this;this.adapter.activateInputRipple(),requestAnimationFrame((function(){t.adapter.deactivateInputRipple()}))},e}(r.K);var s=i(78220),d=i(18601),c=i(14114),p=i(37500),h=i(33310),f=i(8636);class m extends s.H{constructor(){super(...arguments),this.alignEnd=!1,this.spaceBetween=!1,this.nowrap=!1,this.label="",this.mdcFoundationClass=l}createAdapter(){return{registerInteractionHandler:(t,e)=>{this.labelEl.addEventListener(t,e)},deregisterInteractionHandler:(t,e)=>{this.labelEl.removeEventListener(t,e)},activateInputRipple:async()=>{const t=this.input;if(t instanceof d.Wg){const e=await t.ripple;e&&e.startPress()}},deactivateInputRipple:async()=>{const t=this.input;if(t instanceof d.Wg){const e=await t.ripple;e&&e.endPress()}}}}get input(){var t,e;return null!==(e=null===(t=this.slottedInputs)||void 0===t?void 0:t[0])&&void 0!==e?e:null}render(){const t={"mdc-form-field--align-end":this.alignEnd,"mdc-form-field--space-between":this.spaceBetween,"mdc-form-field--nowrap":this.nowrap};return p.dy`
      <div class="mdc-form-field ${(0,f.$)(t)}">
        <slot></slot>
        <label class="mdc-label"
               @click="${this._labelClick}">${this.label}</label>
      </div>`}click(){this._labelClick()}_labelClick(){const t=this.input;t&&(t.focus(),t.click())}}(0,o.__decorate)([(0,h.Cb)({type:Boolean})],m.prototype,"alignEnd",void 0),(0,o.__decorate)([(0,h.Cb)({type:Boolean})],m.prototype,"spaceBetween",void 0),(0,o.__decorate)([(0,h.Cb)({type:Boolean})],m.prototype,"nowrap",void 0),(0,o.__decorate)([(0,h.Cb)({type:String}),(0,c.P)((async function(t){var e;null===(e=this.input)||void 0===e||e.setAttribute("aria-label",t)}))],m.prototype,"label",void 0),(0,o.__decorate)([(0,h.IO)(".mdc-form-field")],m.prototype,"mdcRoot",void 0),(0,o.__decorate)([(0,h.vZ)("",!0,"*")],m.prototype,"slottedInputs",void 0),(0,o.__decorate)([(0,h.IO)("label")],m.prototype,"labelEl",void 0)},92038:(t,e,i)=>{i.d(e,{W:()=>o});const o=i(37500).iv`.mdc-form-field{-moz-osx-font-smoothing:grayscale;-webkit-font-smoothing:antialiased;font-family:Roboto, sans-serif;font-family:var(--mdc-typography-body2-font-family, var(--mdc-typography-font-family, Roboto, sans-serif));font-size:0.875rem;font-size:var(--mdc-typography-body2-font-size, 0.875rem);line-height:1.25rem;line-height:var(--mdc-typography-body2-line-height, 1.25rem);font-weight:400;font-weight:var(--mdc-typography-body2-font-weight, 400);letter-spacing:0.0178571429em;letter-spacing:var(--mdc-typography-body2-letter-spacing, 0.0178571429em);text-decoration:inherit;text-decoration:var(--mdc-typography-body2-text-decoration, inherit);text-transform:inherit;text-transform:var(--mdc-typography-body2-text-transform, inherit);color:rgba(0, 0, 0, 0.87);color:var(--mdc-theme-text-primary-on-background, rgba(0, 0, 0, 0.87));display:inline-flex;align-items:center;vertical-align:middle}.mdc-form-field>label{margin-left:0;margin-right:auto;padding-left:4px;padding-right:0;order:0}[dir=rtl] .mdc-form-field>label,.mdc-form-field>label[dir=rtl]{margin-left:auto;margin-right:0}[dir=rtl] .mdc-form-field>label,.mdc-form-field>label[dir=rtl]{padding-left:0;padding-right:4px}.mdc-form-field--nowrap>label{text-overflow:ellipsis;overflow:hidden;white-space:nowrap}.mdc-form-field--align-end>label{margin-left:auto;margin-right:0;padding-left:0;padding-right:4px;order:-1}[dir=rtl] .mdc-form-field--align-end>label,.mdc-form-field--align-end>label[dir=rtl]{margin-left:0;margin-right:auto}[dir=rtl] .mdc-form-field--align-end>label,.mdc-form-field--align-end>label[dir=rtl]{padding-left:4px;padding-right:0}.mdc-form-field--space-between{justify-content:space-between}.mdc-form-field--space-between>label{margin:0}[dir=rtl] .mdc-form-field--space-between>label,.mdc-form-field--space-between>label[dir=rtl]{margin:0}:host{display:inline-flex}.mdc-form-field{width:100%}::slotted(*){-moz-osx-font-smoothing:grayscale;-webkit-font-smoothing:antialiased;font-family:Roboto, sans-serif;font-family:var(--mdc-typography-body2-font-family, var(--mdc-typography-font-family, Roboto, sans-serif));font-size:0.875rem;font-size:var(--mdc-typography-body2-font-size, 0.875rem);line-height:1.25rem;line-height:var(--mdc-typography-body2-line-height, 1.25rem);font-weight:400;font-weight:var(--mdc-typography-body2-font-weight, 400);letter-spacing:0.0178571429em;letter-spacing:var(--mdc-typography-body2-letter-spacing, 0.0178571429em);text-decoration:inherit;text-decoration:var(--mdc-typography-body2-text-decoration, inherit);text-transform:inherit;text-transform:var(--mdc-typography-body2-text-transform, inherit);color:rgba(0, 0, 0, 0.87);color:var(--mdc-theme-text-primary-on-background, rgba(0, 0, 0, 0.87))}::slotted(mwc-switch){margin-right:10px}[dir=rtl] ::slotted(mwc-switch),::slotted(mwc-switch[dir=rtl]){margin-left:10px}`},56887:(t,e,i)=>{i.d(e,{F:()=>s});var o=i(87480),r=(i(54040),i(37500)),n=i(33310),a=i(8636),l=i(61092);class s extends l.K{constructor(){super(...arguments),this.left=!1,this.graphic="control"}render(){const t={"mdc-deprecated-list-item__graphic":this.left,"mdc-deprecated-list-item__meta":!this.left},e=this.renderText(),i=this.graphic&&"control"!==this.graphic&&!this.left?this.renderGraphic():r.dy``,o=this.hasMeta&&this.left?this.renderMeta():r.dy``,n=this.renderRipple();return r.dy`
      ${n}
      ${i}
      ${this.left?"":e}
      <span class=${(0,a.$)(t)}>
        <mwc-checkbox
            reducedTouchTarget
            tabindex=${this.tabindex}
            .checked=${this.selected}
            ?disabled=${this.disabled}
            @change=${this.onChange}>
        </mwc-checkbox>
      </span>
      ${this.left?e:""}
      ${o}`}async onChange(t){const e=t.target;this.selected===e.checked||(this._skipPropRequest=!0,this.selected=e.checked,await this.updateComplete,this._skipPropRequest=!1)}}(0,o.__decorate)([(0,n.IO)("slot")],s.prototype,"slotElement",void 0),(0,o.__decorate)([(0,n.IO)("mwc-checkbox")],s.prototype,"checkboxElement",void 0),(0,o.__decorate)([(0,n.Cb)({type:Boolean})],s.prototype,"left",void 0),(0,o.__decorate)([(0,n.Cb)({type:String,reflect:!0})],s.prototype,"graphic",void 0)},21270:(t,e,i)=>{i.d(e,{W:()=>o});const o=i(37500).iv`:host(:not([twoline])){height:56px}:host(:not([left])) .mdc-deprecated-list-item__meta{height:40px;width:40px}`},25782:(t,e,i)=>{i(10994),i(65660),i(70019),i(97968);var o=i(9672),r=i(50856),n=i(33760);(0,o.k)({_template:r.d`
    <style include="paper-item-shared-styles"></style>
    <style>
      :host {
        @apply --layout-horizontal;
        @apply --layout-center;
        @apply --paper-font-subhead;

        @apply --paper-item;
        @apply --paper-icon-item;
      }

      .content-icon {
        @apply --layout-horizontal;
        @apply --layout-center;

        width: var(--paper-item-icon-width, 56px);
        @apply --paper-item-icon;
      }
    </style>

    <div id="contentIcon" class="content-icon">
      <slot name="item-icon"></slot>
    </div>
    <slot></slot>
`,is:"paper-icon-item",behaviors:[n.U]})},89194:(t,e,i)=>{i(10994),i(65660),i(70019);var o=i(9672),r=i(50856);(0,o.k)({_template:r.d`
    <style>
      :host {
        overflow: hidden; /* needed for text-overflow: ellipsis to work on ff */
        @apply --layout-vertical;
        @apply --layout-center-justified;
        @apply --layout-flex;
      }

      :host([two-line]) {
        min-height: var(--paper-item-body-two-line-min-height, 72px);
      }

      :host([three-line]) {
        min-height: var(--paper-item-body-three-line-min-height, 88px);
      }

      :host > ::slotted(*) {
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }

      :host > ::slotted([secondary]) {
        @apply --paper-font-body1;

        color: var(--paper-item-body-secondary-color, var(--secondary-text-color));

        @apply --paper-item-body-secondary;
      }
    </style>

    <slot></slot>
`,is:"paper-item-body"})},22142:(t,e,i)=>{i.d(e,{C:()=>p});var o=i(15304),r=i(38941),n=i(81563),a=i(19596);class l{constructor(t){this.U=t}disconnect(){this.U=void 0}reconnect(t){this.U=t}deref(){return this.U}}class s{constructor(){this.Y=void 0,this.q=void 0}get(){return this.Y}pause(){var t;null!==(t=this.Y)&&void 0!==t||(this.Y=new Promise((t=>this.q=t)))}resume(){var t;null===(t=this.q)||void 0===t||t.call(this),this.Y=this.q=void 0}}const d=t=>!(0,n.pt)(t)&&"function"==typeof t.then;class c extends a.s{constructor(){super(...arguments),this._$Cft=1073741823,this._$Cwt=[],this._$CG=new l(this),this._$CK=new s}render(...t){var e;return null!==(e=t.find((t=>!d(t))))&&void 0!==e?e:o.Jb}update(t,e){const i=this._$Cwt;let r=i.length;this._$Cwt=e;const n=this._$CG,a=this._$CK;this.isConnected||this.disconnected();for(let t=0;t<e.length&&!(t>this._$Cft);t++){const o=e[t];if(!d(o))return this._$Cft=t,o;t<r&&o===i[t]||(this._$Cft=1073741823,r=0,Promise.resolve(o).then((async t=>{for(;a.get();)await a.get();const e=n.deref();if(void 0!==e){const i=e._$Cwt.indexOf(o);i>-1&&i<e._$Cft&&(e._$Cft=i,e.setValue(t))}})))}return o.Jb}disconnected(){this._$CG.disconnect(),this._$CK.pause()}reconnected(){this._$CG.reconnect(this),this._$CK.resume()}}const p=(0,r.XM)(c)}}]);
//# sourceMappingURL=4ca0f749.js.map