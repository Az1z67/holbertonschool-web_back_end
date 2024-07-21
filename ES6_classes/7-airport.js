export default class Airport {
  constructor(code, name) {
    this._code = '';
    this._name = '';

    this.code = code;
    this.name = name;
  }

  toString() {
    return `[object ${this._code}]`;
  }
}
