# Parallelismo

**Applicazione Concorrente**: abbiamo due o più thread in esecuzione in un momento. Ad esempio vengono scambiati con il processore dal SO.

**Applicazione Parallela:** abbiamo due o più thread che vengono eseguiti nello stesso momento se il processore ha più core.  
Parallelismo $\subseteq$ Concorrenza (se ho un solo thread, ovviamente degenera in una programmazione concorrente).

---

La maggior parte degli algoritmi odierni sono sequenziali: specificano una sequenza di passi in cui ogni passo consiste in una singola operazione.  
Un algoritmo parallelo è progettato per eseguire più operazioni nello stesso passo e può offrire prestazioni migliori su molti tipi diversi di computer.

Le operazioni in un algoritmo parallelo possono essere eseguite simultaneamente da diversi processori o core.  
![[Screenshot 2025-09-16 alle 16.56.06.png]]  
Non si ha alcuna conoscenza dell’ordine con cui le istruzioni vengono eseguite.

È necessario sincronizzare i flussi per evitare le _race conditions_, il metodo più tipico è utilizzare i lock, i mutex e i semafori.

mutex $\rightarrow$ killer delle prestazioni

Quindi solitamente il locking e i mutex sono molto costosi per le operazioni su CPU. Le operazioni su GPU non permettono l’uso di locking e mutex.  
Ci sono altre soluzioni.  
L’obiettivo è fare un codice veloce, **NON SICURO**.

Evitare il più possibile la sincronizzazione dei thread.

Invece di utilizzare strutture dati complesse, meglio usare allocazioni di memoria.

![[Screenshot 2025-09-16 alle 17.16.01.png]]

Dopo un po’ vediamo che le performance single-thread rimangono costanti: di conseguenza la strada migliore è utilizzare tutti i core con thread.

La frequenza di clock di un processore non può essere aumentata senza causare surriscaldamento. Ma:

- Sempre più processori possono essere integrati nello stesso spazio.
    
- I multicore sono ovunque.
    

---

# Parallelo e Distribuito

La **Programmazione Parallela** serve a risolvere un singolo problema in modo veloce, mentre il **Calcolo Distribuito** viene usato per convenienza, in termini di disponibilità, affidabilità e accessibilità da molte località diverse.

Tipicamente: interazioni poco frequenti, con maggiore peso e presunte inaffidabili, granularità grossolana, molto overhead e lunghi tempi di uptime.

---

# Potenza e Consumo

La potenza è proporzionale alla frequenza per il quadrato del voltaggio.

$$P \propto V^2 \cdot f $$ 
$$V \propto f$$
Quindi: $$P \propto f^3$$

Aumentando la frequenza, la stessa quantità di lavoro può essere terminata prima (~ inversamente alla frequenza), quindi l’energia richiesta è:  
$$E \propto f^2 $$

Il parallelismo può essere utilizzato per conservare energia e quindi consumare meno potenza.  
![[Screenshot 2025-09-16 alle 17.24.43.png]]

Le GPU richiedono molta energia ma, grazie al parallelismo aumentato, possono ridurre il consumo.  
È vantaggioso che i core siano più numerosi rispetto ai task da svolgere, così che i core non lavorino a pieno regime e il consumo complessivo sia inferiore rispetto a un mono-thread.

---

Supponiamo di dover calcolare in un secondo:

`for (i = 0; i < ONE_TRILLION; i++)     z[i] = x[i] + y[i];`

Quindi dobbiamo effettuare $3 \times 10^{12}$ spostamenti di memoria al secondo.

- Se i dati viaggiano alla velocità della luce ($3 \times 10^8$ m/s) tra CPU e memoria,  
    e $r$ è la distanza media tra CPU e memoria, allora $r$ deve soddisfare:
    

$$3×1012⋅r=3×108⋅13 \times 10^{12} \cdot r = 3 \times 10^8 \cdot 13×1012⋅r=3×108⋅1$$  
che dà $r = 10^{-4}$ metri.

Creando un quadrato con la CPU al centro, otteniamo:  
$$(2⋅10−4)2(2 \cdot 10^{-4})^2(2⋅10−4)2$$

Per inserire i dati in un quadrato in modo che la distanza media dalla CPU sia $r$, la lunghezza di ogni cella (quadrata) di memoria sarà:

2⋅10−43⋅106=10−10 m\frac{2 \cdot 10^{-4}}{\sqrt{3 \cdot 10^6}} = 10^{-10} \, m3⋅106​2⋅10−4​=10−10m

che è la dimensione di un atomo relativamente piccolo!

**NON È FISICAMENTE POSSIBILE!**

---

A volte il parallelismo è dannoso!

I programmi paralleli scritti male possono essere peggiori delle loro controparti sequenziali:

- Più lenti: a causa dell’overhead di comunicazione.
    
- Scalabilità: alcuni algoritmi paralleli sono più veloci solo quando il problema è molto grande.
    
- Bisogna comprendere il problema e usare il buon senso!
    
- Inoltre: non tutti i problemi possono essere parallelizzati.
    

---

# Tipi di Parallelismi

Ci sono diversi livelli di parallelismo:

- **Bit-Level Parallelism:** é una forma di parallelismo basato sull'aumentare della dimensione delle word che puó elaborare una CPU. 
  se ho una CPU a 8 bit, leggo 8 bit alla volta. Se devo sommare due valori da 32 bit ciascuno, devo fare un ciclo che legge 8 bit per volta. Con una CPU a 32 bit lo faccio in modo piú veloce.
    
- **Instruction-Level Parallelism:** ![[Screenshot 2025-09-16 alle 17.48.16.png]]
    
- **Data Parallelism:** tutte le CPU moderne possono lavorare con parole di dati molto grandi in parallelo. **SIMD** (Single Instruction, Multiple Data). L’elaborazione multimediale è un buon candidato per questo tipo di architettura.
    
- **Task-Level Parallelism:** due varianti importanti, legate al modello di memoria sottostante: condivisa vs. distribuita.
    
    - **Shared memory multiprocessors:** ogni CPU accede a qualunque locazione di memoria, la comunicazione (IPC) avviene tramite memoria. Di conseguenza si ha uno scambio di messaggi scrivendo nella memoria del core corrispondente.
        
    - **Distributed memory system:** ogni CPU ha la sua memoria locale, la comunicazione avviene tramite rete.
        
I **Shared Memory systems** sono più semplici ma non scalano oltre un certo numero di processori. I sistemi distribuiti sono la strada da seguire per sistemi fault-tolerant.

---

## Shared Memory System

![[Screenshot 2025-09-16 alle 17.59.45.png]]  
I nostri personal computer sono **Shared Memory System**.
La caratteristica di questi sistemi sono dati dal fatto che la memoria é condivisa tra piú **core**. Ogni core si interfaccia prima con la **cache** e poi con la memoria.

I lati positivi sono che sono facili da usare attraverso il multithreading

Mentre quelli negativi sono che possono esserci *race conditions* ed é molto piú difficile debuggare.

---

## Distributed Memory System

![[Screenshot 2025-09-16 alle 18.05.21.png]]  
I processori possono accedere solo alla loro memoria e comunicano tramite messaggi.
Richiede il minimo supporto hardware.
Più facile da debuggare: 
- Le interazioni avvengono in parti ben definite del programma.
- Il processo controlla la sua memoria!
È necessario un protocollo di comunicazione complesso.
I dati remoti non possono essere acceduti direttamente, ma solo tramite richiesta.

---

## Sistema Eterogeneo

Se ho una CPU e una GPU allora ho un **sistema eterogeneo**, dove ciascuna componente ha la propria memoria.  
La CPU gestisce il flusso di controllo e la logica complessa, la GPU processa un grande dataset in parallelo e si hanno dei chip specializzati (TPU e FPGA) che ottimizzano specifiche operazioni.
![[Screenshot 2025-09-16 alle 18.08.25.png]]

---
# Tassonomia di Flynn


![[Screenshot 2025-09-17 184652.png]]
![[Pasted image 20250917184756.png]]

___
# Architetture Parallele

- **Random Access Machine (RAM):** è un modello astratto di calcolatore sequenziale.
    
    - Modella un dispositivo con un’unità di esecuzione istruzioni e memoria illimitata.
        
    - La memoria contiene istruzioni e dati.
        
    - Qualunque locazione può essere letta in tempo unitario.
        
    - L’unità di esecuzione carica ed esegue un’istruzione ogni ciclo.
        
    - I computer moderni si discostano dalla RAM, ma funzionano come se rispettassero questo modello.


Anche nei sistemi a memoria condivisa ci sono differenze di prestazioni in base alla distanza dalla RAM.

- **PRAM (Parallel Random Access Machine):** modello astratto di calcolatore parallelo.
    
    - Modella un dispositivo con un numero indefinito di unità di esecuzione istruzioni e memoria globale illimitata accessibile uniformemente.
        
    - Fallisce perché rappresenta male il comportamento della memoria.
        
    - È impossibile realizzare un’unica immagine di memoria a tempo unitario quando più unità accedono alla stessa locazione.
        
    - Una cattiva modellazione della memoria porta a valutazioni errate degli algoritmi: le prestazioni predette da PRAM non si verificano nei computer reali!
- CTA (Candidate Type Architecture): anche questo é un modello astratto di architettura.
  - separa esplicitamejnte due tipi di indirizzi di memoria:
	  - indirizzi di memoria locali non costosi
	  - e costosi.
	 ![[Pasted image 20250917190309.png]] 


---
![[Pasted image 20250917193701.png]]
___
Nella realtá si ha il modello di programmazione CUDA, questo é fatto chiaramente attraverso una gerarchia di memoria ben definita.

In una GPU ci sono diversi tipi di memoria, organizzati in una gerarchia che bilancia **velocità**, **capacità** e **visibilità**:

- **Global memory**
    
    - È la DRAM presente sulla scheda GPU.
        
    - Ha grande capacità (GB), ma è molto **lenta**: i tempi di accesso sono centinaia di cicli di clock.
        
    - È condivisa tra **tutti i thread** di tutti i blocchi.
        
    - Se i thread leggono e scrivono continuamente da qui, si crea un **collo di bottiglia**.
        
- **Shared memory**
    
    - È una memoria **piccola ma veloce** (pochi KB per blocco).
        
    - È condivisa **solo tra i thread di uno stesso blocco**.
        
    - È gestita dal programmatore (devi decidere tu cosa caricarci dentro).
        
    - Funziona un po’ come una cache manuale: prendi i dati lenti dalla global memory, li copi qui, e poi li riusi velocemente.
# Metriche di valutazione delle performance

- **Stream**: sequenza (anche infinita) di valori dello stesso tipo (es. immagini come matrici).
    
- **Service time (tempo di servizio)**: tempo medio tra due elaborazioni consecutive → misura il _throughput_.
    
- **Completion time (tempo di completamento)**: tempo medio per completare l’elaborazione di **tutti** gli elementi dello stream.
    
- **Latency (latenza)**: tempo medio per elaborare **un singolo elemento**.
    

⚠️ Nota: con **valori singoli** (non stream) ha senso parlare di _completion time_, ma non di _service time_.
___
## Modulo Sequenziale (Σ)

- Ogni operazione ha un tempo medio $t_i$ e una probabilità di occorrenza $p_i$.
    
- **Service time medio**:  
    $$t=\sum_{i=1}^k p_i t_i$$
    
- **Bandwidth (throughput)**:  
    $$B= \frac{1}{t}$$
    
- **Completion time (per uno stream lungo $m$):**  
    $$t_c=m \cdot t$$
    
- **Latency:** coincide col _service time_ (perché il sistema è sequenziale).

---

## Modulo Parallelo (Σ → Σₙ con n moduli)

- **Parallelism degree**: $n$ (numero di moduli, indipendente da quanto realmente lavorano in parallelo).
    
- **Service time ($t_n$):** tempo medio tra due input consecutivi accettati.
    
- **Bandwidth (throughput):**  
    $$B_n = \frac{1}{t_n}$$
    
- **Completion time (per stream lungo $m$):**  
    $$t_{c_n} \approx m \cdot t_n \quad \text{(per $m \gg n$)}$$
    
- **Latency:** tempo medio per processare un singolo elemento (può differire dal service time).
    

---

## Differenze Sequenziale vs Parallelo

- **Sequenziale:**
    
    - _Latency_ = _Service time_.
        
- **Parallelo:**
    
    - _Service time_ ≠ _Latency_.
        
    - _Service time_ misura l’intervallo dopo cui il sistema può accettare un nuovo input, anche se non ha ancora completato l’output del precedente.
        
    - _Latency_ può aumentare rispetto al sequenziale (es. nel _pipelining_).

___
