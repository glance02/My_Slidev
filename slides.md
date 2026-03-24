---
theme: dracula
layout: cover
background: https://images.unsplash.com/photo-1677442136019-21780ecad995?w=1920
---

# Transformer 代码实战

从注意力机制到完整架构

<div class="pt-12">
  <span class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press <kbd>Space</kbd> to next
  </span>
</div>

---
layout: center
class: text-center
---

# 什么是 Transformer?

2017年 Google 在论文 **"Attention Is All You Need"** 中提出

- 完全基于**注意力机制**的序列转换模型
- 取代了传统的 RNN 和 CNN
- 成为现代 NLP 的基石

---
layout: two-cols
---

# Transformer 整体架构

::right::

<img src="https://production-media.paperswithcode.com/methods/transformer_architecture.png" width="500" />

::left::

**编码器 (Encoder)**

- Multi-Head Self-Attention
- Feed Forward Network
- 6 层堆叠

<br/>

**解码器 (Decoder)**

- Masked Self-Attention
- Cross Attention
- Feed Forward Network

---
layout: center
---

# 核心组件: Self-Attention

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class SelfAttention(nn.Module):
    def __init__(self, embed_size, heads):
        super(SelfAttention, self).__init__()
        self.embed_size = embed_size
        self.heads = heads
        self.head_dim = embed_size // heads

        assert self.head_dim * heads == embed_size, "Embedding size must be divisible by heads"

        self.values = nn.Linear(embed_size, embed_size)
        self.keys = nn.Linear(embed_size, embed_size)
        self.queries = nn.Linear(embed_size, embed_size)
        self.fc_out = nn.Linear(embed_size, embed_size)

    def forward(self, values, keys, query, mask):
        N = query.shape[0]
        value_len, key_len, query_len = values.shape[1], keys.shape[1], query.shape[1]

        # Split into heads
        values = values.reshape(N, value_len, self.heads, self.head_dim)
        keys = keys.reshape(N, key_len, self.heads, self.head_dim)
        queries = query.reshape(N, query_len, self.heads, self.head_dim)

        values = self.values(values)
        keys = self.keys(keys)
        queries = self.queries(queries)
```

---
layout: two-cols
---

# Attention 计算过程

::right::

```python
# Scaled Dot-Product Attention
energy = torch.einsum("nqhd,nkhd->nhqk", [queries, keys])

if mask is not None:
    energy = energy.masked_fill(mask == 0, float("-1e20"))

attention = F.softmax(energy / math.sqrt(self.head_dim), dim=3)

out = torch.einsum("nhql,nlhd->nqhd", [attention, values]).reshape(
    N, query_len, self.heads * self.head_dim
)

return self.fc_out(out)
```

::left::

1. **QKV 变换**: 将输入投影到 Query、Key、Value 空间

2. **计算注意力分数**: Query 与 Key 做点积

3. **缩放**: 除以 $\sqrt{d_k}$ 防止梯度消失

4. **Softmax**: 得到注意力权重

5. **加权求和**: Value 乘以注意力权重

---

# 多头注意力机制

```python
class MultiHeadAttention(nn.Module):
    def __init__(self, embed_size, num_heads, dropout=0.1):
        super(MultiHeadAttention, self).__init__()
        self.attention = SelfAttention(embed_size, num_heads)
        self.norm = nn.LayerNorm(embed_size)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask=None):
        # Pre-norm 架构
        x = self.norm(x)
        attn_out = self.attention(x, x, x, mask)
        return self.dropout(attn_out) + x  # 残差连接
```

<div class="text-center pt-4">

**多头注意力的优势**:

- 多个注意力头可以捕获不同类型的依赖关系
- 每个头学习不同的注意力模式
- 并行计算，效率高

</div>

---
layout: two-cols
---

# 位置编码 (Positional Encoding)

::right::

```python
class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=5000):
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(
            0, max_len, dtype=torch.float
        ).unsqueeze(1)

        div_term = torch.exp(
            torch.arange(0, d_model, 2)
            * (-math.log(10000.0) / d_model)
        )

        pe[:, 0::2] = torch.sin(
            position * div_term
        )
        pe[:, 1::2] = torch.cos(
            position * div_term
        )
        pe = pe.unsqueeze(0)
        self.register_buffer(
            'pe', pe
        )

    def forward(self, x):
        return x + self.pe[:, :x.size(1)]
```

::left::

因为 Transformer 没有循环结构，需要**显式注入位置信息**

使用正弦和余弦函数编码位置:

$$PE_{(pos,2i)} = \sin(pos / 10000^{2i/d_{model}})$$

$$PE_{(pos,2i+1)} = \cos(pos / 10000^{2i/d_{model}})$$

---

# 完整 Transformer Encoder

```python {1-2|4-8|10-14|16-20|all}
class TransformerEncoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout=0.1):
        super().__init__()
        self.self_attn = MultiHeadAttention(d_model, num_heads, dropout)
        self.ff = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.GELU(),
            nn.Linear(d_ff, d_model)
        )
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask=None):
        # Self-attention with residual
        x = x + self.dropout(self.self_attn(self.norm1(x), mask))
        # Feed-forward with residual
        x = x + self.dropout(self.ff(self.norm2(x)))
        return x
```

---

# 完整 Transformer 解码器

```python {1-3|5-11|13-17|19-23|all}
class TransformerDecoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout=0.1):
        super().__init__()
        self.self_attn = MultiHeadAttention(d_model, num_heads, dropout)
        self.cross_attn = MultiHeadAttention(d_model, num_heads, dropout)
        self.ff = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.GELU(),
            nn.Linear(d_ff, d_model)
        )
        self.norms = nn.ModuleList([nn.LayerNorm(d_model) for _ in range(3)])

    def forward(self, x, enc_output, tgt_mask=None, src_mask=None):
        # Masked self-attention
        x = x + self.dropout(self.self_attn(self.norms[0](x), tgt_mask))
        # Cross-attention with encoder output
        x = x + self.dropout(self.cross_attn(self.norms[1](x), enc_output, enc_output, src_mask))
        # Feed-forward
        x = x + self.dropout(self.ff(self.norms[2](x)))
        return x
```

---
layout: center
---

# 经典代码示例: 简化 Transformer

```python
class Transformer(nn.Module):
    def __init__(self, src_vocab, tgt_vocab, d_model=512,
                 num_heads=8, num_layers=6, d_ff=2048, dropout=0.1):
        super().__init__()
        self.encoder = nn.ModuleList([
            TransformerEncoderLayer(d_model, num_heads, d_ff, dropout)
            for _ in range(num_layers)
        ])
        self.decoder = nn.ModuleList([
            TransformerDecoderLayer(d_model, num_heads, d_ff, dropout)
            for _ in range(num_layers)
        ])
        self.src_embed = nn.Embedding(src_vocab, d_model)
        self.tgt_embed = nn.Embedding(tgt_vocab, d_model)
        self.pos_enc = PositionalEncoding(d_model)
        self.fc = nn.Linear(d_model, tgt_vocab)

    def forward(self, src, tgt, src_mask=None, tgt_mask=None):
        src = self.pos_enc(self.src_embed(src))
        tgt = self.pos_enc(self.tgt_embed(tgt))

        enc_output = src
        for layer in self.encoder:
            enc_output = layer(enc_output, src_mask)

        dec_output = tgt
        for layer in self.decoder:
            dec_output = layer(dec_output, enc_output, tgt_mask, src_mask)

        return self.fc(dec_output)
```

---

# Transformer 应用场景

<div class="grid grid-cols-2 gap-4 pt-4">

<div class="p-4 rounded shadow-lg bg-gradient-to-br from-blue-500 to-purple-600 text-white">

**NLP 任务**

- Machine Translation
- Text Summarization
- Question Answering
- Sentiment Analysis

</div>

<div class="p-4 rounded shadow-lg bg-gradient-to-br from-green-500 to-teal-600 text-white">

**多模态任务**

- Vision Transformer (ViT)
- CLIP / DALL-E
- Video Understanding
- Speech Processing

</div>

<div class="p-4 rounded shadow-lg bg-gradient-to-br from-orange-500 to-red-600 text-white">

**大语言模型**

- GPT 系列
- BERT 系列
- LLaMA / ChatGLM
- Mistral

</div>

<div class="p-4 rounded shadow-lg bg-gradient-to-br from-purple-500 to-pink-600 text-white">

**前沿研究**

- Instruction Tuning
- RLHF
- Chain-of-Thought
- Mixture of Experts

</div>

</div>

---
layout: center
class: text-center
---

# 总结

<div class="text-2xl">

- **Attention** 是 Transformer 的核心
- **多头注意力** 捕获多种依赖模式
- **位置编码** 注入序列位置信息
- **残差连接** 支持深层网络训练

</div>

<div class="pt-12 text-gray-400">

下一步: 尝试实现一个简单的翻译模型!

</div>
