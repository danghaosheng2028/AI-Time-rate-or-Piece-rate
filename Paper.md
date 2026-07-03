# From Hours to Output: Risk‑Sharing, Incentives, and Contract Transformation under AI‑Augmented Production

Lucas Dang  
RCF Experimental School, Beijing  
July 2026

---

## Abstract

Rapid advances in artificial intelligence (AI) have transformed how firms allocate tasks, monitor performance, and design compensation systems. While AI increases productivity, it also amplifies output volatility and reshapes the allocation of risk between firms and workers. This paper develops a principal–agent model of AI‑augmented production in which effective human capital is:

$$\tilde{H} = h + \theta AC,$$

where $A$ denotes AI utilization intensity and $C$ captures human–AI complementarity. Firms choose between a time‑rate contract with enforceable minimum effort and a piece‑rate contract that requires digital monitoring and exposes workers to output risk.

We derive closed‑form expressions for optimal effort, optimal piece‑rate incentives, and firm profit under each contract. A central theoretical result is the existence of a unique contract transformation threshold $A^*$ such that firms optimally switch from time‑rate to piece‑rate compensation once AI intensity exceeds this level. The threshold arises because time‑rate profit grows linearly in $A$, whereas piece‑rate profit grows convexly due to incentive amplification and AI‑enhanced productivity.

Using the implicit function theorem, we characterize the comparative statics of $A^*$. The threshold increases in output noise and worker risk aversion—reflecting the cost of risk exposure under piece‑rate pay—and decreases in human–AI complementarity, which strengthens incentive effectiveness. Numerical simulations confirm these results and quantify how China’s minimum‑wage regulation systematically delays contract transformation by raising the required base wage under piece‑rate compensation.

The model provides a unified explanation for heterogeneous adoption of output‑based pay across industries and offers policy insights on labor regulation, AI‑skills training, and the future of incentive design in AI‑enabled workplaces.

---

## Keywords

AI‑augmented production;  
principal–agent model;  
risk‑sharing;  
incentive design;  
contract transformation;  
piece‑rate compensation;  
time‑rate compensation;  
human–AI complementarity;  
minimum‑wage regulation;  
comparative statics.

---

# 1. Introduction

Artificial intelligence (AI) is transforming how firms organize production, monitor performance, and design compensation systems. In China, this transformation is particularly salient: more than 84 million workers were engaged in platform‑based flexible employment in 2023, accounting for roughly 15 percent of urban employment. Since the 2021 *Guiding Opinions on Safeguarding the Labor Rights of New Employment Forms*, platform labor has become a regulated category, and the shift from traditional time‑rate compensation to output‑based pay has accelerated across logistics, content creation, and digital services.

Yet this transition presents a fundamental economic paradox. AI technologies increase productivity by augmenting workers’ effective human capital, but they also amplify output volatility and expose workers to greater income risk. Under piece‑rate compensation, workers bear both effort costs and output risk, whereas under time‑rate compensation, firms shoulder the risk while enforcing minimum effort through observable inputs. This raises a central question:

**Under what conditions should firms switch from time‑rate to piece‑rate compensation, and how does AI adoption shift this boundary?**

Existing research provides important foundations but leaves this question open. Classical principal–agent theory (Holmstrom 1979; Holmstrom & Milgrom 1991) establishes that optimal linear contracts balance incentives against risk exposure. Recent work on AI and labor markets documents productivity gains from AI adoption but does not analyze how AI changes contract design. Emerging studies argue that AI may shift firms toward output‑based pay, yet they do not provide a closed‑form characterization of the transformation threshold or its comparative statics.

This paper fills that gap by embedding AI into a tractable principal–agent model. We introduce an AI‑augmented effective human capital function:

$$\tilde{H} = h + \theta AC,$$

derive closed‑form expressions for optimal effort and incentives, and show that a unique transformation threshold $A^*$ exists. Comparative statics reveal how noise, risk aversion, and human–AI complementarity shape this threshold. We further incorporate China’s minimum‑wage regulation and show that binding wage floors systematically delay contract transformation.

The remainder of the paper proceeds as follows. Section 2 reviews the related literature. Section 3 presents stylized facts and parameter calibration. Section 4 introduces the model. Section 5 derives equilibrium outcomes. Section 6 presents the main theoretical results. Section 7 provides numerical simulations. Section 8 concludes with policy implications. Appendices contain additional proofs and calibration details.

---

# 2. Literature Review

## 2.1 Principal–Agent Models of Incentives and Risk-Sharing

The theoretical foundation of this paper lies in the canonical principal–agent framework. Holmstrom (1979) establishes that under CARA utility and normally distributed noise, optimal contracts are linear in output and balance incentives against risk exposure. Holmstrom and Milgrom (1991) extend this insight to multi‑task environments, showing that high‑noise tasks favor fixed wages because incentives distort effort allocation.

Subsequent work has refined these insights. Lazear (2000) documents empirically how piece‑rate compensation increases productivity but also raises income volatility. Prendergast (2002) emphasizes the role of uncertainty in shaping incentive strength. These studies highlight the tradeoff between incentives and risk, but they do not incorporate AI as a productivity‑augmenting force nor analyze how AI shifts the optimal contract boundary.

This paper contributes to this literature by embedding AI‑augmented production into the Holmstrom–Milgrom framework. By modeling effective human capital as $\tilde{H}=h+\theta AC$, we show that AI amplifies the incentive effect of piece‑rate contracts and generates a unique transformation threshold $A^*$ at which firms optimally switch from time‑rate to piece‑rate compensation.

## 2.2 AI, Automation, and Labor Markets

A second strand of literature examines how AI and automation reshape labor markets. Acemoglu and Restrepo (2018) develop a task‑based model in which automation reallocates labor across tasks and affects wages and employment. Brynjolfsson, Li, and Raymond (2025) provide empirical evidence that AI tools significantly increase individual productivity in knowledge‑intensive occupations. Other studies document how AI affects monitoring, prediction, and managerial decision‑making.

However, this literature focuses primarily on employment, productivity, and task allocation—not on compensation design. While Shin and Kang (2026) argue conceptually that AI may shift firms toward output‑based pay, they do not provide a closed‑form characterization of the transformation threshold or its comparative statics. No existing model formally links AI adoption to the optimal allocation of risk and incentives within the firm.

## 2.3 Platform Labor, Flexible Employment, and Chinese Labor Regulation

A third strand of literature examines the rise of platform labor and flexible employment in China. Government reports indicate that platform‑based flexible workers exceeded 84 million in 2023, reflecting rapid growth in gig‑economy sectors such as logistics, ride‑hailing, and digital content creation. Scholars have analyzed how platform algorithms shape labor supply, monitoring, and compensation, and how regulatory frameworks attempt to balance flexibility with worker protection.

A central regulatory instrument is the minimum‑wage system, which imposes binding constraints on base wages even in flexible employment arrangements. Recent policy documents emphasize the need to protect workers from excessive income volatility, but they do not analyze how such regulations interact with incentive design or AI adoption.

## 2.4 Contribution Relative to the Literature

Relative to these three strands, the paper makes three contributions:

1. **A closed‑form transformation threshold.**  
   We derive a unique $A^*$ at which firms optimally switch from time‑rate to piece‑rate compensation.

2. **Comparative statics linking risk, uncertainty, and AI complementarity.**  
   Using the implicit function theorem, we show how noise, risk aversion, and human–AI complementarity jointly determine the transformation threshold.

3. **Integration of Chinese labor regulation.**  
   By incorporating minimum‑wage constraints, we provide a theoretical explanation for regulatory frictions that delay contract transformation in China’s rapidly digitalizing labor markets.

---

# 3. Stylized Facts and Parameter Calibration

This section presents three stylized facts that motivate the model and guide the calibration of key parameters. The goal is to anchor the theoretical framework in empirical patterns observed in China’s rapidly digitalizing labor markets and to justify the numerical values used in the simulations in Section 7. The facts correspond directly to the model’s core parameters: AI intensity $A$, human–AI complementarity $C$, output noise $\sigma^2$, and worker risk aversion $r$.

---

## 3.1 Stylized Fact 1: Rising AI Penetration in Chinese Firms

China has experienced a rapid increase in enterprise‑level digitalization and AI adoption. According to the China Academy of Information and Communications Technology (CAICT), the penetration rate of digital tools among Chinese firms rose from roughly 18 percent in 2018 to nearly 40 percent in 2022. Industries such as logistics, e‑commerce operations, content creation, and customer service have adopted AI‑based workflow tools, automated monitoring systems, and algorithmic decision‑making at scale.

This motivates modeling AI intensity $A$ as a continuous variable capturing the degree of AI integration into production. The simulation range $A\in[0,3]$ corresponds to the empirical transition from low to high AI penetration.

---

## 3.2 Stylized Fact 2: Expansion of Flexible and Output‑Based Employment

China’s platform economy has expanded dramatically. Government statistics indicate that platform‑based flexible workers exceeded 84 million in 2023, a 50 percent increase from 2019. These workers include couriers, ride‑hailing drivers, livestream hosts, and digital content creators—occupations where output‑based compensation is increasingly prevalent.

This fact supports the model’s focus on contract transformation from time‑rate to piece‑rate pay. It also motivates the inclusion of a fixed monitoring cost $F$, reflecting the digital infrastructure required to implement output‑based compensation.

---

## 3.3 Stylized Fact 3: Empirical Estimates of Worker Risk Aversion

Labor economics provides empirical guidance on the magnitude of worker risk aversion. Chetty (2006) and subsequent studies estimate absolute risk aversion parameters in the range $r\in[0.2,2.0]$ for typical workers facing income volatility. This range is consistent with observed behavior in gig‑economy occupations.

We therefore set $r=1.0$ as the baseline value and explore the full empirical range in comparative statics.

---

## 3.4 Calibration of Remaining Parameters

To ensure internal consistency and empirical plausibility, the remaining parameters are calibrated as follows:

- Baseline human capital: $h=2.0$  
- AI amplification coefficient: $\theta=1.5$  
- Human–AI complementarity: $C=1.0$  
- Effort cost parameter: $k=1.0$  
- Minimum enforceable effort: $a_0=1.0$  
- Reservation utility: $\bar{U}=1.0$  
- Output noise: $\sigma^2=1.0$  
- Monitoring cost: $F=1.5$

These values jointly produce a baseline transformation threshold $A^*\approx 0.65$, which aligns with mid‑range AI penetration levels in Chinese digital service industries.

---

# 4. Model

This section presents the formal environment of the model. We consider a one‑period principal–agent framework in which a risk‑neutral firm hires a single worker whose effort is not contractible. The firm chooses between two compensation modes—time‑rate and piece‑rate—and AI technology enters the production process by augmenting the worker’s effective human capital.

---

## 4.1 Environment

### Effective human capital

$$\tilde{H} = h + \theta AC.$$

Here:

- $h>0$ is baseline human capital  
- $A\ge 0$ is AI utilization intensity  
- $C>0$ is human–AI complementarity  
- $\theta>0$ is the amplification effect of AI

---

### Production technology

Output is:

$$y = a\tilde{H} + \varepsilon,$$

where $\varepsilon \sim N(0,\sigma^2)$.

---

### Effort cost

Effort incurs convex cost:

$$\psi(a) = \frac{1}{2}ka^2.$$

---

### Worker preferences

The worker has CARA utility with absolute risk aversion $r>0$. Certainty equivalent:

$$CE = E[w] - \frac{1}{2}r\,\mathrm{Var}(w) - \psi(a).$$

---

### Moral hazard

Effort $a$ is not observable or contractible.

---

### Participation constraint

Competitive labor markets imply:

$$CE = \bar{U}.$$

---

## 4.2 Time‑Rate Contract (Mode T)

Under time‑rate compensation:

- Worker receives fixed wage $W_0$  
- Firm enforces minimum effort $a_0$

Participation constraint:

$$W_0 - \frac{1}{2}ka_0^2 = \bar{U}.$$

Thus:

$$W_0 = \bar{U} + \frac{1}{2}ka_0^2.$$

Firm profit:

$$\Pi_T(A) = a_0(h+\theta AC) - \bar{U} - \frac{1}{2}ka_0^2.$$

This is linear in $A$.

---

## 4.3 Piece‑Rate Contract (Mode P)

Compensation:

$$w = \alpha + \gamma y.$$

### Worker’s effort choice

Worker solves:

$$\max_a\; \gamma a\tilde{H} - \frac{1}{2}ka^2.$$

Thus:

$$a^* = \frac{\gamma\tilde{H}}{k}.$$

---

### Participation constraint

Certainty equivalent:

$$
CE = \alpha
+ \gamma a^*\tilde{H}
- \frac{1}{2}r\gamma^2\sigma^2
- \frac{1}{2}k(a^*)^2.
$$

Substitute $a^*$:

$$
CE = \alpha
+ \frac{\gamma^2\tilde{H}^2}{k}
- \frac{1}{2}r\gamma^2\sigma^2
- \frac{1}{2k}\gamma^2\tilde{H}^2.
$$

Simplify:

$$
CE = \alpha
+ \frac{1}{2k}\gamma^2\tilde{H}^2
- \frac{1}{2}r\gamma^2\sigma^2.
$$

Set $CE=\bar{U}$:

$$
\alpha
= \bar{U}
+ \frac{1}{2}r\gamma^2\sigma^2
- \frac{1}{2k}\gamma^2\tilde{H}^2.
$$

---

### Firm profit

Expected profit:

$$
\Pi_P(\gamma)
= (1-\gamma)a^*\tilde{H} - \alpha - F.
$$

Substitute $a^*$ and $\alpha$:

$$
\Pi_P(\gamma)
= \frac{\gamma\tilde{H}^2}{k}
- \frac{1}{2k}\gamma^2\tilde{H}^2
- \frac{1}{2}r\gamma^2\sigma^2
- \bar{U} - F.
$$

---

### Optimal piece‑rate

FOC yields:

$$
\gamma^*
= \frac{\tilde{H}^2}{\tilde{H}^2 + rk\sigma^2}.
$$

Optimal profit:

$$
\Pi_P^*(A)
= \frac{\tilde{H}^4}{2k(\tilde{H}^2 + rk\sigma^2)}
- \bar{U} - F.
$$

---

## 4.4 Timing

1. Firm chooses contract mode.  
2. Under piece‑rate, firm chooses $(\alpha,\gamma)$.  
3. Worker chooses effort $a$.  
4. Output realized; wage paid.

---

## 4.5 Discussion

The model embeds AI into the Holmstrom–Milgrom linear contracting framework by allowing AI intensity $A$ and complementarity $C$ to scale effective human capital. AI amplifies both productivity and the returns to effort, altering the firm’s optimal risk‑sharing arrangement and potentially triggering contract transformation.

# 5. Equilibrium Analysis

This section derives the equilibrium outcomes under the two compensation modes introduced in Section 4. We first characterize the firm’s profit under the time‑rate contract, which is linear in AI intensity. We then solve the worker’s incentive problem under the piece‑rate contract, derive the optimal piece‑rate parameter, and obtain the firm’s optimal profit. The comparison of these two profit functions forms the basis for the contract transformation threshold analyzed in Section 6.

---

## 5.1 Time‑Rate Contract (Mode T)

Under the time‑rate contract, the firm enforces a minimum effort level $a_0$ through attendance monitoring. The worker receives a fixed wage $W_0$, and her certainty equivalent is:

$$CE_T = W_0 - \frac{1}{2}ka_0^2.$$

The participation constraint $CE_T = \bar{U}$ implies:

$$W_0 = \bar{U} + \frac{1}{2}ka_0^2.$$

The firm’s expected profit is therefore:

$$\Pi_T(A)
= a_0(h+\theta AC) - \bar{U} - \frac{1}{2}ka_0^2.$$

This profit is **linear** in AI intensity $A$:

$$\frac{d\Pi_T}{dA} = a_0\theta C.$$

---

## 5.2 Piece‑Rate Contract (Mode P)

Under the piece‑rate contract:

$$w = \alpha + \gamma y.$$

The firm chooses $(\alpha,\gamma)$ to satisfy incentive compatibility (IC) and individual rationality (IR), and to maximize expected profit.

---

### Step 1: Incentive Compatibility (IC)

Worker chooses effort $a$ to maximize:

$$CE_P(a)
= \alpha + \gamma a\tilde{H}
- \frac{1}{2}r\gamma^2\sigma^2
- \frac{1}{2}ka^2.$$

FOC yields:

$$a^* = \frac{\gamma\tilde{H}}{k}.$$

---

### Step 2: Participation Constraint (IR)

Substitute $a^*$:

$$
CE_P = \alpha
+ \frac{1}{2k}\gamma^2\tilde{H}^2
- \frac{1}{2}r\gamma^2\sigma^2.
$$

Set $CE_P=\bar{U}$:

$$
\alpha
= \bar{U}
+ \frac{1}{2}r\gamma^2\sigma^2
- \frac{1}{2k}\gamma^2\tilde{H}^2.
$$

---

### Step 3: Firm Profit Maximization

Expected profit:

$$
\Pi_P(\gamma)
= (1-\gamma)a^*\tilde{H} - \alpha - F.
$$

Substitute $a^*$ and $\alpha$:

$$
\Pi_P(\gamma)
= \frac{\gamma\tilde{H}^2}{k}
- \frac{1}{2k}\gamma^2\tilde{H}^2
- \frac{1}{2}r\gamma^2\sigma^2
- \bar{U} - F.
$$

FOC yields optimal piece‑rate:

$$
\gamma^*
= \frac{\tilde{H}^2}{\tilde{H}^2 + rk\sigma^2}.
$$

Optimal profit:

$$
\Pi_P^*(A)
= \frac{\tilde{H}^4}{2k(\tilde{H}^2 + rk\sigma^2)}
- \bar{U} - F.
$$

---

## 5.3 Comparison of the Two Modes

Define profit difference:

$$G(A) = \Pi_P^*(A) - \Pi_T(A).$$

Section 6 shows:

- $G(0)<0$ due to fixed cost $F$  
- $G(A)\to+\infty$ as $A\to\infty$  
- $G(A)$ is strictly increasing for large $A$

Thus a unique threshold $A^*$ exists.

---

# 6. Main Results

This section presents the core theoretical results of the paper. We show that AI‑augmented production generates a unique threshold in AI utilization intensity at which firms optimally switch from time‑rate to piece‑rate compensation. We then characterize how this threshold responds to changes in output noise, worker risk aversion, and human–AI complementarity.

---

## 6.1 Existence and Uniqueness of the Contract Transformation Threshold

Define:

$$G(A) = \Pi_P^*(A) - \Pi_T(A).$$

---

### **Theorem 1 (Existence and uniqueness of $A^*$).**

There exists a **unique** threshold $A^*>0$ such that:

- For $A < A^*$: $\Pi_T(A) > \Pi_P^*(A)$  
- For $A > A^*$: $\Pi_P^*(A) > \Pi_T(A)$

---

### Proof

#### Step 1: Existence

At $A=0$:

$$G(0) < 0.$$

As $A\to\infty$:

$$\Pi_T(A) \sim a_0\theta C A,$$

$$\Pi_P^*(A) \sim \frac{(\theta C)^2}{2k}A^2.$$

Thus:

$$G(A)\to+\infty.$$

By continuity, at least one root exists.

---

#### Step 2: Uniqueness

$\Pi_T(A)$ is linear.  
$\Pi_P^*(A)$ is strictly convex:

$$\frac{d^2\Pi_P^*(A)}{dA^2} > 0.$$

A convex function minus a linear function crosses zero **once**.

$\blacksquare$

---

## 6.2 Comparative Statics of the Transformation Threshold

Using implicit function theorem:

$$\frac{\partial A^*}{\partial x}
= -\frac{\partial G/\partial x}{\partial G/\partial A},
\qquad x\in\{\sigma^2,r,C\}.$$

Denominator:

$$\frac{\partial G}{\partial A}(A^*) > 0.$$

---

### (i) Noise $\sigma^2$

$$
\frac{\partial \Pi_P^*}{\partial \sigma^2}
= -\frac{r\tilde{H}^4}{2(\tilde{H}^2 + rk\sigma^2)^2} < 0.
$$

Thus:

$$\frac{\partial A^*}{\partial \sigma^2} > 0.$$

---

### (ii) Risk aversion $r$

$$
\frac{\partial \Pi_P^*}{\partial r}
= -\frac{\sigma^2\tilde{H}^4}{2(\tilde{H}^2 + rk\sigma^2)^2} < 0.
$$

Thus:

$$\frac{\partial A^*}{\partial r} > 0.$$

---

### (iii) Human–AI complementarity $C$

$$\frac{\partial \tilde{H}}{\partial C} = \theta A > 0.$$

Higher $C$ increases convexity of $\Pi_P^*(A)$:

$$\frac{\partial A^*}{\partial C} < 0.$$

---

## 6.3 Implications for Contract Design

The results imply:

1. Risk and uncertainty delay transformation.  
2. Human–AI complementarity accelerates transformation.  
3. AI amplifies incentives, making piece‑rate increasingly attractive as $A$ grows.

These insights form the theoretical foundation for Section 7’s numerical simulations.

# 7. Numerical Simulation

This section presents numerical simulations that illustrate the theoretical results derived in Sections 5 and 6. Using the calibrated parameters from Section 3, we evaluate firm profit under the time‑rate and piece‑rate contracts, compute the contract transformation threshold $A^*$, and examine how risk, uncertainty, and regulation affect the profitability of output‑based compensation.

All simulations use the baseline parameter set:

$$(h,\theta,C,k,a_0,\bar{U},r,\sigma^2,F) = (2.0,1.5,1.0,1.0,1.0,1.0,1.0,1.0,1.5).$$

---

## 7.1 Baseline Profit Comparison and the Transformation Threshold

We compute:

- Time‑rate profit:  
  $$\Pi_T(A) = a_0(h+\theta AC) - \bar{U} - \frac{1}{2}ka_0^2.$$

- Piece‑rate profit:  
  $$\Pi_P^*(A) = \frac{\tilde{H}^4}{2k(\tilde{H}^2 + rk\sigma^2)} - \bar{U} - F,$$
  where $\tilde{H}=h+\theta AC$.

Plotting $\Pi_T(A)$ and $\Pi_P^*(A)$ for $A\in[0,3]$ yields a unique intersection at:

$$A^* \approx 0.65.$$

Interpretation:

- For $A < A^*$: fixed monitoring cost $F$ makes piece‑rate unprofitable.  
- For $A > A^*$: convex productivity gains dominate, making piece‑rate optimal.

This confirms Theorem 1.

---

## 7.2 Comparative Statics: Threshold Surface $A^*(r,\sigma^2)$

We compute $A^*$ over a grid:

- $r\in[0.1,2.0]$  
- $\sigma^2\in[0.1,2.0]$

For each pair, solve $G(A)=0$.

Results:

- $A^*$ increases in $r$  
- $A^*$ increases in $\sigma^2$  
- $A^*$ decreases in $C$

These match Theorem 2.

---

## 7.3 Regulatory Friction: Minimum Wage Constraint

Introduce minimum wage:

$$\alpha \ge W_{\min}.$$

This raises the required base wage under piece‑rate compensation:

$$\alpha_{MW} = \max\left\{W_{\min},\; \bar{U}
+ \frac{1}{2}r\gamma^2\sigma^2
- \frac{1}{2k}\gamma^2\tilde{H}^2\right\}.$$

Profit becomes:

$$\Pi_P^{MW}(A) = (1-\gamma)a^*\tilde{H} - \alpha_{MW} - F.$$

The new threshold satisfies:

$$A^*_{MW} > A^*.$$

Regulatory delay:

$$\Delta A = A^*_{MW} - A^*.$$

Interpretation:

- Minimum wage pushes firms to stay longer in time‑rate mode.  
- Explains why some Chinese industries remain time‑rate dominated despite high digitalization.

---

## 7.4 Summary of Simulation Results

1. Piece‑rate profit is convex in $A$.  
2. Time‑rate profit is linear in $A$.  
3. A unique transformation threshold exists.  
4. Noise and risk aversion delay transformation.  
5. Human–AI complementarity accelerates transformation.  
6. Minimum‑wage regulation postpones transformation.

---

# 8. Conclusion and Policy Implications

This paper develops a principal–agent model of compensation design under AI‑augmented production. By embedding AI intensity $A$ and human–AI complementarity $C$ into effective human capital $\tilde{H}=h+\theta AC$, we derive closed‑form expressions for optimal effort, optimal piece‑rate incentives, and firm profit under time‑rate and piece‑rate contracts.

A central theoretical result is the existence of a unique transformation threshold $A^*$ at which firms optimally switch from time‑rate to piece‑rate compensation. Comparative statics show that the threshold increases in output noise and worker risk aversion and decreases in human–AI complementarity. Numerical simulations confirm these results and quantify how minimum‑wage regulation delays contract transformation.

---

## 8.1 Policy Implications

### (1) Differentiated labor regulation across industries

Industries with high AI penetration and strong complementarity (e.g., digital content creation) are likely above $A^*$ and benefit from output‑based pay.  
Low‑AI or high‑noise industries remain below $A^*$, where time‑rate compensation is optimal.

### (2) Human–AI complementarity training

Because $A^*$ decreases in $C$, policies that enhance workers’ ability to collaborate with AI tools can accelerate beneficial contract transformation.

### (3) Minimum‑wage design for flexible employment

Binding wage floors raise the required base wage under piece‑rate compensation, delaying transformation.  
Hybrid systems (minimum income guarantees, earnings smoothing) may protect workers without distorting incentives.

---

## 8.2 Limitations and Future Research

1. Noise is assumed Gaussian; AI prediction errors may be heavy‑tailed.  
2. Multi‑agent extensions could analyze team production under AI.  
3. Dynamic models could incorporate learning about AI tools.

---

# Appendix A. Additional Proofs for Comparative Statics

We provide full derivations for:

- $\frac{\partial A^*}{\partial r} > 0$  
- $\frac{\partial A^*}{\partial C} < 0$

---

## A.1 Derivative with Respect to Risk Aversion $r$

Piece‑rate profit:

$$
\Pi_P^*(A)
= \frac{\tilde{H}^4}{2k(\tilde{H}^2 + rk\sigma^2)}
- \bar{U} - F.
$$

Differentiate:

$$
\frac{\partial \Pi_P^*}{\partial r}
= -\frac{\sigma^2\tilde{H}^4}{2(\tilde{H}^2 + rk\sigma^2)^2} < 0.
$$

Thus:

$$\frac{\partial A^*}{\partial r} > 0.$$

---

## A.2 Derivative with Respect to Complementarity $C$

Effective human capital:

$$\tilde{H} = h + \theta AC.$$

Thus:

$$\frac{\partial \tilde{H}}{\partial C} = \theta A > 0.$$

Higher $C$ increases convexity of $\Pi_P^*(A)$:

$$\frac{\partial A^*}{\partial C} < 0.$$

---

# Appendix B. Parameter Calibration Details

## B.1 Human Capital and AI Amplification

- $h=2.0$  
- $\theta=1.5$  
- $C=1.0$

## B.2 Effort Cost and Monitoring

- $k=1.0$  
- $a_0=1.0$  
- $\bar{U}=1.0$  
- $F=1.5$

## B.3 Noise and Risk Aversion

- $\sigma^2=1.0$  
- $r=1.0$

## B.4 AI Intensity Range

$A\in[0,3]$ corresponds to empirical digitalization levels in Chinese firms.

Baseline threshold:

$$A^*\approx 0.65.$$

---

# References

Acemoglu, D., & Restrepo, P. (2018). *The Race Between Man and Machine*.  
Brynjolfsson, E., Li, Y., & Raymond, L. (2025). *Productivity Effects of AI Tools*.  
Chetty, R. (2006). *A New Method for Estimating Risk Aversion*.  
Holmstrom, B. (1979). *Moral Hazard and Observability*.  
Holmstrom, B., & Milgrom, P. (1991). *Multitask Principal–Agent Problems*.  
Lazear, E. (2000). *Performance Pay and Productivity*.  
Prendergast, C. (2002). *The Tenuous Tradeoff Between Risk and Incentives*.  
Shin, J., & Kang, H. (2026). *AI and Compensation Systems*.  

