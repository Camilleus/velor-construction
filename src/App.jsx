import React from 'react';
import Navbar from './components/Navbar';
import Hero from './sections/Hero';
import Oferta from './sections/Oferta';
import Kariera from './sections/Kariera';
import Kontakt from './sections/Kontakt';
import Footer from './components/Footer';

function App() {
  return (
    <div className="bg-background text-white min-h-screen selection:bg-accent selection:text-white">
      <Navbar />
      <main>
        <Hero />
        <Oferta />
        <Kariera />
        <Kontakt />
      </main>
      <Footer />
    </div>
  );
}

export default App;
