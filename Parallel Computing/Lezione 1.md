# Parallelismo
**Applicazione Concorrente**: abbiamo due o più thread in sviluppo in un momento. Ad esempio viene scambiato con il processore dal SO.

**Applicazione Parallela:** abbiamo due o più thread che vengono eseguite nello stesso momento se il processore ha più core.
Parallelismo $\subseteq$ Concorrente (se ho un thread e basta degenera ovviamente in una programmazione concorrente.)


Most of today’s algorithms are sequential: they specify a sequence of steps in which each step consists of a single operation. 
A parallel algorithm is designed to execute multiple operations at the same step and it can yield improved performance on many different kinds of computers.

The operations in a parallel algorithm can be performed simultaneously by different processors or cores.
![[Screenshot 2025-09-16 alle 16.56.06.png]]
Non hai nessuna conoscenza dell'ordine delle istruzioni con il quale vengono eseguite le istruzioni. 

Bisogna sincronizzare i flussi per evitare *race conditions*, il più tipico per sincronizzare è utilizzare i locks, mutex, semafori.

mutex $\rightarrow$ performance killer

Quindi solitamente locking e mutex è molto costosa per le operazioni CPU. Le operazioni su GPU non permettono utilizzo di locking e mutex.
Ci sono altre strade.
Obiettivo è fare un codice veloce NON SICURO.

Evitare il più possibile la sincronizzazione dei thread.

Invece di utilizzare data structure ma allocazioni di memoria. 

![[Screenshot 2025-09-16 alle 17.16.01.png]]

Dopo un pò vediamo che le performance single thread rimangono costanti, di conseguenza la strada migliore è utilizzare tutti i core con thread.

The clock speed of a processor cannot be increased without overheating But:
- More and more processors can fit in the same space.
- Multicores are everywhere.
# Parallelo e Distribuito
Parallel Programming serve a risolvere un solo problema in modo veloce mentre il Distribuited Computing è per convenienza, in terms of availability, reliability and accessibility from many different locations. Typically: interactions infrequent, with heavier weight and assumed to be unreliable, coarse grained, much overhead and long uptime.

# Potenza Consumo

La potenza è proporzionale alla frequenza per il quadrato del voltaggio.

$$P \propto V^2 \cdot f$$
$$V \propto f$$
Quindi: $$P \propto f^3$$
Increasing the frequency, the same amount of work can be finished earlier (~ inversely to the frequency), so the required energy is: $$E \propto f^2 $$
Il parallelismo può essere utilizzato per conservare energia e quindi consumare meno potenza.
![[Screenshot 2025-09-16 alle 17.24.43.png]]
GPUs need lot of power but thanks to increased parallelism they can reduce consumption.
E' un bene che i core siano tanti rispetto ai task che devono essere fatti, così che i core non eseguono a pieno regime e quindi il consumo generale è minore rispetto a un mono thread.

Suppose we have to calculate in one second:
for (i = 0; i < ONE_TRILLION; i++)
	z\[i\] = x\[i\] + y\[i\];

Then we have to perform 3x1012 memory moves per second 
• If data travels at the speed of light (3x108 m/s) between the CPU and memory, 
and r is the average distance between the CPU and memory,  then r must satisfy • 3×1012 r = 3×108 m/s × 1 s which gives r = 10-4 meters 

Creiamolo quadrato la CPU quindi:
$(2\cdot10^{-4})^2$ 

• To fit the data into a square so that the average distance from the CPU in the middle is r, then the length of each (square) memory cell will be 

• 2×10-4 m / (√3×106) = 10-10 m which is the size of a relatively small atom!

IT CANNOT BE DONE PHISICALLY!

___
Sometimes parallel is bad!

Bad parallel programs can be worse than their sequential counterparts:
• Slower: because of communication overhead.
• Scalability: some parallel algorithms are only faster when the problem size is very large 
• Understand the problem and use common sense! 
• Moreover: not all problems are be parallelised.
# Tipi di Parallelismi
Ci sono diversi livelli di parallelismo:
- Bit level Parallelism: ho una cpu a 8bit quindi ho una scrittura di 8bit a volta. Se voglio sommare due valori da 32bit l'uno. C'è un for in cui leggo 8bit a volta. Con una CPU da 32 bit la faccio in 3 operazioni. 
- Instruction-Level Parallelism: ![[Screenshot 2025-09-16 alle 17.48.16.png]]
- Data Parallelism: tutte le CPU moderne hanno delle operazioni possono lavorare con veramente grosse parole di dati in parallelo. SIMD (Single Instruction, Multiple Data). Multimedia processing is a good candidate for this type of architecture.
- Task-Level Parallelism: There are two important variations, related to the underlying memory model: shared vs. distributed.
	• Shared memory multiprocessors: each CPU accesses any memory location, IPC is done through memory. 
	• Distributed memory system: each CPU has its own local memory, IPC is done through a network. 
	• Shared memory systems are simpler but do not scale after a certain number of processors: Distributed systems are the way to go for fault-tolerant systems. IPC (Intern Process Communication)
## Shared memory system
 ![[Screenshot 2025-09-16 alle 17.59.45.png]]
Our personal computer are cores (Shared Memory System).

## Distributed Memory System:
![[Screenshot 2025-09-16 alle 18.05.21.png]]
Processors can only access their own memory and communicate through messages. • Requires the least hardware support. 
• Easier to debug. 
• Interactions happens in well-defined program parts 
• The process is in control of its memory! 
• Cumbersome communication protocol is needed • Remote data cannot be accessed directly, only via request.

## Eterogeneous System:

Se ho una CPU e una GPU allora ho un sistema eterogeneo dove le due componenti avranno una memoria per ognuno.

![[Screenshot 2025-09-16 alle 18.08.25.png]]

# Architetture Parallele:
Random Access Machine: is an abstract model for a sequential computer 
	• It models a device with an instruction execution unit and unbounded memory.
	• Memory stores program instructions and data. 
	• Any memory location can be referenced in ‘unit’ time 
	• The instruction unit fetches and executes an instruction every cycle and proceeds to the next instruction. 
	• Today’s computers depart from RAM, but function as if they match this model.

Anche nelle Shared Memory System ci sono delle differenze di prestazioni data dalla distanza dalla RAM.

Nel modello PRAM (Parallel Random Access Machine): abstract model for parallel computer 
• It models a device with an unspecified number of instruction execution units and global memory of unbounded size that is uniformly accessible to all processors 
• It fails by misrepresenting memory behavior. 
• Impossible to realize the unit-time single memory image when multiple exec. units access the same location 
• Bad memory modeling leads to wrong evaluation of algorithms: PRAM’s performance predictions are not observed in real computers !

(altro)

# Metriche di valutazione delle performance:

(completare)
