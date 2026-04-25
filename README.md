# Semgrep 作业报告

## 1. 选择的漏洞 / 坏模式
本次规则集覆盖了 7 类常见 Python 安全风险：
- 动态代码执行（eval/exec/compile）
- 命令注入（subprocess shell=True）
- 不安全反序列化（pickle）
- 弱加密哈希（MD5/SHA1）
- 硬编码密码/密钥
- assert 滥用（优化模式下失效）
- 路径穿越（open 用户输入）

**重点关注**：命令注入与路径穿越，因为它们在实际扫描中命中。

## 2. 为什么适合写成规则（可重复判据）
这些模式都具有**明确的语法特征**，例如：
- `subprocess.run(..., shell=True)` 中的 `shell=True` 参数
- `open($PATH)` 其中 `$PATH` 不是字符串字面量
- `hashlib.md5(` 的函数名

人工审计可以总结为“只要出现这些模式，且不使用排除模式，就应告警”。Semgrep 能够将这些判据固化为 `pattern` 或 `pattern-either`，实现可重复、可回归的自动化检测。

## 3. 规则解释（关键 pattern 与排除条件）
以 `python.command-injection.shell-true` 为例：
```yaml
patterns:
  - pattern: subprocess.$FUNC(..., shell=True, ...)
  - metavariable-regex:
      metavariable: $FUNC
      regex: ^(run|call|check_output|Popen)$
